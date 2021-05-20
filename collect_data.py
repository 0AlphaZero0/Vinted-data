# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 00:00:00 2021

@author: Arthur Thouvenin
contact: athouvenin [at] outlook.com
"""

import requests
import json
import re

# api_url = "https://www.vinted.fr/api/v2/items?search_text=&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&status_ids=&country_ids=&city_ids=&is_for_swap=0&page=1&per_page="
url = "https://www.vinted.fr/vetements?search_text=&brand_id[]=&color_id[]="
url_search_txt = "https://www.vinted.fr/vetements?search_text="
# brands_url = "https://www.vinted.fr/brands"
# catalogs_url = "https://www.vinted.fr/data/search-json.js"
data_repository = "./DATA/"
applicationJSON = r'<script type="application/json" data-js-react-on-rails-store="MainStore">([^<]+)</script>'

id_supported = {
    "catalog":{
        "regex":applicationJSON,
        "nested":"catalogs",
        "names":["title","code"],
        "mainStore":"catalogs",
        "url_name":"catalog[]"
        },
    "color":{
        "regex":applicationJSON,
        "names":["title","code"],
        "mainStore":"colors",
        "url_name":"color_id[]"
        },
    "brand":{
        "names":["title","slug"],
        "url_name":"brand_id[]"
        },
    "size":{
        "regex":applicationJSON,
        "nested":"sizes",
        "names":["title"],
        "only_string":True,
        "mainStore":"sizeGroups",
        "url_name":"size_id[]"
        },
    "material":{
        "regex":applicationJSON,
        "nested":"materials",
        "names":["title","code"],
        "mainStore":"materialGroups",
        "url_name":"material_id[]"
        },
    "status":{
        "regex":applicationJSON,
        "names":["title"],
        "mainStore":"statuses",
        "url_name":"status_id[]"
        },
    "country":{
        "regex":applicationJSON,
        "names":["title","title_local","iso_code"],
        "mainStore":"countries",
        "url_name":"country_id[]"
        }
    }


def JSONfromID(id_names=["catalog","color","brand","size","material","status","country"],id_range=range(0,100),per_page=24,save=False,empty_ids=False):
    """
    This function will extract information from Vinted about the ids requested.

    Parameters
    ----------
    id_names : LIST or STRING, optional
        This parameter indicate which ids you want to extract from Vinted. The default is ["catalog","color","brand","size","material","status","country"].
    id_range : RANGE, optional
        This parameter is used to extract a range of ids for example from 0 to 1000. This parameter is only used to extract brand ids. The default is range(0,100).
    per_page : INTEGER, optional
        This parameter is the number of item per page in the resulting response the best to extract ids corresponds to 24. The default is 24.
    save : BOOLEAN, optional
        This parameter is used to saved ids found in the DATA folder, as following : ./DATA/*id_name*.json. The default is False.
    empty_ids : BOOLEAN, optional
        This parameter is used only for the brand id results. Indeed some brands ids point to nothing, if you want those empty ids in your results set this parameter to True. The default is False.

    Returns
    -------
    collected_data : DICTIONARY
        This dictrionary will contains every ids found. For example if the id_names parameter was ["color","status"] the dictionary will look like this :
            {
                "color":[
                              {
                                "id": 1,
                                "title": "Noir",
                                "hex": "000000",
                                "order": 1,
                                "code": "BLACK"
                              },
                              {
                                "id": 3,
                                "title": "Gris",
                                "hex": "919191",
                                "order": 2,
                                "code": "GREY"
                              },
                              .
                              .
                              .
                        ],
                "status":[
                              {
                                "id": 6,
                                "title": "Neuf avec \u00e9tiquette",
                                "description": "Article neuf, jamais port\u00e9/utilis\u00e9 avec \u00e9tiquettes ou dans son emballage d\u2019origine.",
                                "explanation": "Article neuf, jamais port\u00e9/utilis\u00e9 avec \u00e9tiquettes ou dans son emballage d\u2019origine.",
                                "explanation_title": "Cet article est flambant neuf ?",
                                "is_default": 0,
                                "order": 5
                              },
                              {
                                "id": 1,
                                "title": "Neuf sans \u00e9tiquette",
                                "description": "Article neuf, jamais port\u00e9/utilis\u00e9, sans \u00e9tiquettes ni emballage d\u2019origine.",
                                "explanation": "Article neuf, jamais port\u00e9/utilis\u00e9, sans \u00e9tiquettes ni emballage d\u2019origine.",
                                "explanation_title": "L\u2019article n\u2019a plus d\u2019\u00e9tiquette, mais il n\u2019a jamais \u00e9t\u00e9 port\u00e9 ?",
                                "is_default": 0,
                                "order": 10
                              },
                              .
                              .
                              .
                        ]
              }

    """
    
    def brandIds(id_name,id_supported,id_range=id_range,per_page=per_page,empty_ids=empty_ids):
        """
        This function will extract a range of brand ids from Vinted and their corresponding information.

        Parameters
        ----------
        id_name : STRING
            This parameter is not used here but essential.
        id_supported : DICTIONARY
            This parameter is not used here but essential.
        id_range : RANGE, optional
            This parameter is used to extract a range of ids for example from 0 to 1000. This parameter is only used to extract brand ids. The default is range(0,100).
        per_page : INTEGER, optional
            This parameter is the number of item per page in the resulting response the best to extract ids corresponds to 24. The default is 24.
        empty_ids : BOOLEAN, optional
            This parameter is used only for the brand id results. Indeed some brands ids point to nothing, if you want those empty ids in your results set this parameter to True. The default is False.

        Returns
        -------
        id_DATA : LIST
            This list will contains every brand ids found and their corresponding information.

        """

        def chunks(lst, n):
            """
            This function will create sublists of size n from the list lst.

            Parameters
            ----------
            lst : LIST
                This parameter is not used here but essential.
            n : INTEGER
                This parameter is not used here but essential.
            
            Returns
            -------
            None

            """
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        chunk_size = 50
        id_DATA = []
        ids_to_scan = chunks([i for i in id_range],chunk_size)
        x = 0
        for chunk in ids_to_scan:
            x += 1
            chunk = [str(s) for s in chunk]
            new_url = url_search_txt+"&brand_id[]="+"&brand_id[]=".join(chunk)
            req = requests.get(new_url).text
            brands = re.findall(r"({\"id\":[0-9]+,\"title\":\"[^\"]+\",\"slug\":[^}]+})", req)
            for brand in brands:
                brand = json.loads(brand)
                if brand not in id_DATA:
                    id_DATA.append(brand)
            print("#######################\n"+id_name.split("_")[0].capitalize()+" ID Extraction...")
            print(new_url)
            print("Ids processed : "+str(x*chunk_size))
            print("IDs found : "+str(len(id_DATA)))
        return id_DATA

    def params(id_supported,id_names=id_names):
        """
        This function will format the id_names as a list.

        Parameters
        ----------
        id_names : STRING or LIST, optional
            A list or string that should correpond to one of the supported Vinted IDs. The default is id_names.
        id_supported : DICTIONARY
            A dictionary containing supported Vinted IDs and their corresponding information

        Returns
        -------
        id_names : LIST
            A list of supported Vinted IDs.

        """

        def check_supported_ids(id_names=id_names,id_supported=id_supported):
            """
            This function will check if all ids in id_name are supported.

            Parameters
            ----------
            id_names : list, optional
                A list or string that should correpond to one of the supported Vinted IDs. The default is id_names.
            id_supported : TYPE, optional
                A dictionary containing supported Vinted IDs and their corresponding information. The default is id_supported.

            Returns
            -------
            BOOLEAN
            """
            id_not_supported = []
            for i in id_names:
                if i not in id_supported:
                    id_not_supported.append(i)
            if len(id_not_supported) != 0:
                raise(f'Following ids are not supported currently ({id_names}), please check supported ids.\n {str_id_supp}')
            return True

        if isinstance(id_names, str) and id_names in id_supported:
            return [id_names]
        if isinstance(id_names, list) and check_supported_ids(id_names,id_supported):
            return id_names
        str_id_supp = id_supported.keys()
        raise(f'Following id is not supported currently ({id_names}), please check supported ids.\n {str_id_supp}')
        
    def regexMatching(id_name,id_supported):
        """
        This function will, from an ID name, extract the corresponding Python object from Vinted with a regex matching.

        Parameters
        ----------
        id_name : STRING
            A string corresponding to a supported Vinted ID.
        id_supported : DICTIONARY
            Dictionary which contains Vinted IDs and their corresponding information.

        Returns
        -------
        id_DATA : JSON - PYTHON OBJECT
            Python object corresponding to the JSON found in Vinted data corresponding to the id_name.

        """
        req = requests.get(url).text
        id_DATA = json.loads(re.findall(id_supported[id_name]["regex"], req)[0])
        if "mainStore" in id_supported[id_name]:
            return id_DATA["catalogFilters"]["dtos"][id_supported[id_name]["mainStore"]]
        return id_DATA

    def colorModification(id_DATA):
        """
        This function will add the # to the hex field of the Python object corresponding to the ID color in Vinted.

        Parameters
        ----------
        id_DATA : JSON - PYTHON OBJECT
            The python object collected for the color ID.

        Returns
        -------
        id_DATA : JSON - PYTHON OBJECT
            The same python object collected for the color ID, but with the # in front of the hex values.

        """
        for color in id_DATA:
            color["hex"] = "#"+color["hex"]
        return id_DATA
    

    id_supported["color"]["modification"] = colorModification
    id_supported["brand"]["function"] = brandIds

    for i in id_supported:
        if "regex" in id_supported[i]:
            id_supported[i]["function"] = regexMatching

    id_names = params(id_supported)
    collected_data = {}
    for id_name in id_names:
        id_DATA = id_supported[id_name]["function"](id_name,id_supported)
        if "modification" in id_supported[id_name]:
            id_DATA = id_supported[id_name]["modification"](id_DATA)
        collected_data[id_name]=id_DATA
        print(id_name.capitalize()+" found : "+str(len(id_DATA)))

    if save:
        for id_collected in collected_data:
            with open("./DATA/"+id_collected+".json",'w') as outfile:
                json.dump(collected_data[id_collected],outfile,indent=2)
    return collected_data

def searchVinted(searchText="",catalog=[],color=[],brand=[],size=[],material=[],status=[],country=[],price_to=1000000,price_from=0,currency="EUR",per_page=120,page=1):
    """
    This function try to a programmatic way to search for item within Vinted thanks to Vinted data extract everyday and store in the folder DATA.

    Parameters
    ----------
    searchText : STRING, optional
        A string that will correspond to a search with the Vinted search bar.
    catalog : LIST, optional
        A list of specific IDs or catalog names.
    color : LIST, optional
        A list of specific IDs or color names.
    brand : LIST, optional
        A list of specific IDs or brand names.
    size : LIST, optional
        A list of specific IDs or size names.
    material : LIST, optional
        A list of specific IDs or material names.
    status : LIST, optional
        A list of specific IDs or status names.
    country : LIST, optional
        A list of specific IDs or country names.
    price_to : INTEGER, optional
        A maximum price fix as the max limit.
    price_from : INTEGER, optional
        A minimum price fix as the min limit.
    currency : STRING, optional
        The currency in which you want the prices.
    per_page : INTEGER, optional
        The number of items per page in your result.
    page : INTEGER, optional
        The page index.
    
    Return
    ------
    --- : DICTIONARY
        This function will return a dictionary looking like :
        {
            "items": [item1,item2,item3,item4,...,itemN],
            "searchParams":{Parameters of the search within Vinted}
        }
    """


    def matchingIDs(ID_name,IDs):
        """
        This function will try to match the information provided as ID to the data corresponding to the ID_name.
        For example if we provide the ID_name 'color', we can either provide an integer ID or a string such as 'pink' for the corresponding color.

        Parameters
        ----------
        ID_name : STRING
            An ID name corresponding to one of the supported id within id_supported.
        IDs : LIST
            A list of integer or string corresponding to IDs found within Vinted data.
        
        Return
        ------
        IDs_requested : LIST
            A list of matched IDs corresponding to information provided in IDs.

        """
        
        def findID(ID_name,ID,data):
            """
            This function will try to match an ID to the 'ID' provided, it can either be an integer or a string corresponding to a term inside the title of ID for example 'rose' for the color pink.

            Parameters
            ----------
            ID_name : STRING
                A string that correspond to one if the ID name supported (Check the dictionary id_supported).
            ID : STRING OR INTEGER
                If ID is an integer it will be consider as the ID to look for (except for sizes as these can sometimes be integer), if it is a string then the algorithm will try to match an ID based on the string provided.
            data : LIST
                A list of dictionaries corresponding to one of the JSON file in the DATA folder.
            
            Return
            ------
            --- : LIST
                A list of IDs matched to the string or integer provided as ID.
            """
            def matchNames(ID_name,ID,data):
                """
                This function will return the corresponding ids matched to the ID provided with the parameter data and ID_name. IDs will be matched through a string matching.

                Parameters
                ----------
                ID_name : STRING
                    The name of the ID to check for example if you are looking for 'H&M' brand the ID_name should be 'brand'.
                ID : STRING
                    The string provided to find within the data for example for an ID_name='brand' the ID can be 'Nike'.
                data : LIST
                    A list of dictionaries corresponding to one of the JSON file in the DATA folder.
                
                Return
                ------
                matched_ids : LIST
                    A list of integer corresponding to the IDs matched.
                """
                matched_ids = []
                for data_id in data:
                    if ID.lower() in [data_id[n].lower() for n in id_supported[ID_name]["names"] if n in data_id]:
                        matched_ids.append(data_id["id"])
                return matched_ids

            def isInt(s):
                """
                This function will check if the s object is an integer or not and return the corresponding boolean.

                Parameters
                ----------
                s : PYTHON OBJECT
                    The Python object that need to be checked.
                
                Return
                ------
                A BOOLEAN
                """
                try: 
                    int(s)
                    return True
                except ValueError:
                    return False

            if "only_string" in id_supported[ID_name] and id_supported[ID_name]["only_string"]:
                return matchNames(ID_name,ID,data)
            if isInt(ID):
                return [int(ID)]
            return matchNames(ID_name,ID,data)

        def treeWalk(ID_name,ID,tree):
            """
            Recursive function that will walk through all parents and child of the tree provided as parameter to find the corresponding IDs.

            Parameters
            ----------
            ID_name : STRING
                The name of the ID to check for example if you are looking for 'H&M' brand the ID_name should be 'brand'.
            ID : STRING
                The string provided to find within the data for example for an ID_name='brand' the ID can be 'Nike'.
            tree : LIST
                A list of dictionaries corresponding to one of the JSON file in the DATA folder, ordered as a tree with parents and childs IDs.
            
            Return
            ------
            found_IDs : LIST
                A list of integer corresponding to the IDs matched.

            """

            found_IDs = findID(ID_name,ID,tree)

            # Recursive loop
            for item in tree:
                if id_supported[ID_name]["nested"] in item and len(item[id_supported[ID_name]["nested"]])>0:
                    found_IDs += treeWalk(ID_name,ID,item[id_supported[ID_name]["nested"]])
            return found_IDs

        IDs_requested = []

        # Checking parameters
        if ID_name not in id_supported:
            raise f"{str(ID_name)} not supported please check the following supported IDs {' / '.join(id_supported)}"
        if not isinstance(IDs,list):
            if isinstance(IDs,str):
                IDs = [IDs]
            else:
                raise f"{str(IDs)} must be a string or a list."

        # Loading corresponding data
        with open(file=data_repository+ID_name+".json",mode="r") as f:
            data = json.loads(f.read())

        # Loop through provided information
        for ID in IDs:
            if "nested" in id_supported[ID_name]:
                IDs_requested += treeWalk(ID_name,ID,data)
                tmp = []
                for i in IDs_requested:
                    if i not in tmp:
                        tmp.append(i)
                IDs_requested = tmp
            else:
                IDs_requested += findID(ID_name,ID,data)
        return IDs_requested

    params = {
        "catalog":catalog,
        "color":color,
        "brand":brand,
        "size":size,
        "material":material,
        "status":status,
        "country":country
    }

    url_search = "https://www.vinted.fr/vetements?search_text="+searchText
    url_params = {
        "per_page":per_page,
        "page":page,
        "price_from":price_from,
        "price_to":price_to,
        "currency":currency
    }
    for param in params:
        if len(params[param]) != 0:
            url_params[id_supported[param]["url_name"]]=matchingIDs(param,params[param])
    req = requests.get(url_search,params=url_params)
    print(req.url)
    items = json.loads(re.findall(r'<script type="application/json" data-js-react-on-rails-store="MainStore">([^<]+)</script>',req.text)[0])["items"]
    return {"items":items["byId"],"searchParams":items["catalogItems"]}

def getField(items,field_names=["id"]):
    """
    This function will extract, from the result of Vinted search through searchVinted function, all values of a specific field. For example in each Item there is a field called 'price', with this function you can get a list of all prices from your search.
    
    Parameters
    ----------
    items : LIST
        An item list that corresponds to a list of dictionaries which can be found as the item "items" of the searchVinted response.
    field_names : LIST, optional
        A list of field names provided as strings. For examples , "prices","id","photo",etc.
    
    Returns
    -------
    VALUES : DICTIONARY
        The dictionary will corresponds to the name of the field as the key and the list of values as value.
    
    """
    VALUES = {}
    for field_name in field_names:
        VALUES[field_name] = []
        for item in items:
            if field_name not in items[item]:
                raise f"The field name {field_name} does not exists within the following item :\n {items[item]}"
            VALUES[field_name].append(items[item][field_name])
    return VALUES



if __name__ == '__main__':
    JSONfromID()