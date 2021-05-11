# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 23:18:00 2021

@author: Arthur Thouvenin
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import sys
import pandas as pd
import json
from datetime import datetime


scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
spreadsheet = client.open("Articles")
spreadsheetPublic = client.open("Vinted_Data")

sheet_Articles = spreadsheet.worksheet("Articles")
sheet_Chiffres = spreadsheet.worksheet("Chiffres")


def updateVintedSheets(reload_data=False):
    """
    This function will update the Google spreadsheets containing all of the data found within Vinted.fr temporarly stored in ./DATA/

    Parameters
    ----------
    reload_data : BOOLEAN, optional
        This parameter indicate if the alogrithm need to collect Vinted data before updating the sheets.
    
    Returns
    -------
    None.

    """


    def unPack_Catalogs(json_f):
        """
        This function will return a flatten JSON normalized as a pandas array from the JSON object within the json file (json_f). Thus an embbed JSON will be flatten to a single level layer.
        Catalogs within Vinted are embedded, for example there is a Catalog Accessories corresponding to Men and one for Women and within those Accessories catalogs are mutliple sub-catalogs such as Jewels, etc.
        This function will bring all sub-catalogs and parents catalogs to the same level.

        Parameters
        ----------
        json_f : FILE OBJECT
            The JSON file in which the Catalogs data are stored.
        
        Returns
        -------
        None.

        """


        def recursive_Catalog(json_obj):
            """
            This function wil flaten the JSON object provided as parameter, each field containing a list or dictionary will be deleted.
            Catalogs within Vinted are embedded, for example there is a Catalog Accessories corresponding to Men and one for Women and within those Accessories catalogs are mutliple sub-catalogs such as Jewels, etc.
            This function will bring all sub-catalogs and parents catalogs to the same level.
            """
            field_lists = ["photo","material_group_ids","size_group_ids","package_size_ids"]
            DATA = []     
            for catalog in json_obj:
                for field in field_lists:
                    if field in catalog:
                        del catalog[field]
                if len(catalog["catalogs"])!=0:
                    unpack = recursive_Catalog(catalog["catalogs"])
                    DATA = DATA + unpack
                del catalog["catalogs"]
                DATA.append(catalog)
            return DATA

        json_f = json.load(json_f)
        DATA = pd.json_normalize(recursive_Catalog(json_f))
        return DATA

    def unPack_Materials(json_f):
        json_f = json.load(json_f)
        DATA = []
        for material in json_f:
            title = material["title"]
            for mat in material["materials"]:
                mat["parent"] = title
                DATA.append(mat)
            del material["materials"]
            material["parent"] = title
            DATA.append(material)
        DATA = pd.json_normalize(DATA)
        return DATA

    def unPack_Sizes(json_f):
        json_f = json.load(json_f)
        field_lists = [
            "size_ids"]
        DATA = []
        for size in json_f:
            for field in field_lists:
                if field in size:
                    del size[field]
            parent_title = size["description"]
            parent_id = size["id"]
            if len(size["sizes"]) != 0:
                for s in size["sizes"]:
                    s["parent_id"] = parent_id
                    s["parent_title"] = parent_title
                    DATA.append(s)
            del size["sizes"]
            DATA.append(size)
        DATA = pd.json_normalize(DATA)
        return DATA

    def unPack_Countries(json_f):
        json_f = json.load(json_f)
        field_lists = ["postal_code_constraints"]
        for item in json_f:
            for field in field_lists:
                if field in item:
                    del item[field]
        return pd.json_normalize(json_f)

    def readJSON(json_f):
        return pd.read_json(json_f)

    id_files = {
        "Brand":{
            'function':readJSON
            },
        "Catalog":{
            'function':unPack_Catalogs
            },
        "Color":{
            'function':readJSON
            },
        "Country":{
            'function':unPack_Countries
            },
        "Material":{
            'function':unPack_Materials
            },
        "Size":{
            'function':unPack_Sizes
            },
        "Status":{
            'function':readJSON
            }
        }

    folder = "./DATA/"
    if "JSONfromID" not in sys.modules:
        from collect_data import JSONfromID
    if reload_data:
        JSONfromID(id_range=range(0,10000),per_page=110,save=True)
    for file in os.listdir(folder):
        file_name = file.split(".")[0].capitalize()
        print(file_name)
        with open(folder+file,"r") as json_file:
            data = id_files[file_name]['function'](json_file)
        data.fillna('', inplace=True)
        sheet = spreadsheet.worksheet(file_name)
        sheet.update([data.columns.values.tolist()] + data.values.tolist())
        public_sheet = spreadsheetPublic.worksheet(file_name)
        public_sheet.update([data.columns.values.tolist()] + data.values.tolist())
    now = datetime.now()
    public_sheet = spreadsheetPublic.worksheet("Vinted_Summary")
    public_sheet.update('E12',str(now.strftime("%d-%m-%Y %H:%M")))
    return




if __name__ == '__main__':
    updateVintedSheets(reload_data=True)