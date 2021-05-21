# Vinted-data
 Vinted data & search from [Vinted.fr](https://www.vinted.fr/)


<a href="https://www.reddit.com/r/vinted/comments/jydgir/vinted_api/" target="_blank"> <!-- target _blank opens in new tab-->
  <img src="https://aleen42.github.io/badges/src/reddit.svg" />
</a>
<a href="https://github.com/0AlphaZero0" target="_blank"> <!-- target _blank opens in new tab-->
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</a>
<a href="https://www.linkedin.com/in/arthur-thouvenin-133822135/" target="_blank"> <!-- target _blank opens in new tab-->
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>

 
 
## Vinted data
Vinted data can be visualized in _Google Sheets_ <a href="https://docs.google.com/spreadsheets/d/19CWMW9_0p9b-Qdog4iD9THiY_EY4nabcxF3emalAbqw/edit?usp=sharing" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Google_Sheets_logo_%282014-2020%29.svg/1200px-Google_Sheets_logo_%282014-2020%29.svg.png" width=15/></a> or in a _Google Data Studio_ report <a href="https://datastudio.google.com/reporting/ee24d510-f2ca-48d0-8c08-0ce32adc76f7" target="_blank"><img src="https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg" width=15/></a>. Those are actualized each day at 09:00 (GMT+2) and stored in Google sheets and in this GitHub repository in the folder **[DATA](https://github.com/0AlphaZero0/Vinted-data/tree/main/DATA)**. 


Currently the _BRAND ID_ is the one that take the most time to collect, as I didn't found a query to get all IDs with only one requests or just a few. Currently, data collection for this identifier is done with a query for each brand (more than 2.000 brands currently).

Currently I investigate the [Vinted API](https://www.vinted.fr/api/v2/) to find a better solution than scraping the HTML.


## Vinted search

The Vinted search works perfectly and handle 7 different IDs (catalogs, colors, brands, sizes, materials, status, countries). It returns a dictionary with for the key "items" a list of items found with the Search used. This method can be found within the file collect_data.py. You can therefore use it as follow :

```python
from collect_data import searchVinted

search = searchVinted(
 catalog=[221],
 color=["pink"],
 brand=[53])
```
This should built the corresponding url : https://www.vinted.fr/vetements?search_text=&per_page=120&page=1&price_from=0&price_to=1000000&currency=EUR&catalog%5B%5D=221&color_id%5B%5D=5&brand_id%5B%5D=53

And returns the following dictionary :

<details>
  <summary>Click to expand!</summary>
  
  ```json
    {
      "items": {
        "1101845357": {
          "id": 1101845357,
          "title": "#lot t-shirt taille S",
          "brand_id": 53,
          "size_id": 3,
          "status_id": 3,
          "disposal_conditions": 4,
          "user_id": 20178521,
          "owner_id": null,
          "country_id": 16,
          "catalog_id": 221,
          "color1_id": 5,
          "color2_id": null,
          "package_size_id": 1,
          "is_hidden": 0,
          "is_reserved": 0,
          "reserved_for_user_id": null,
          "is_visible": 1,
          "is_unisex": 0,
          "is_closed": 0,
          "is_admin_alerted": false,
          "active_bid_count": 4,
          "favourite_count": 1,
          "view_count": 37,
          "moderation_status": 0,
          "last_push_up_at": "2021-05-19T22:12:03+02:00",
          "description": "#lot 2 t-shirt \nTaille S\nMarque Nike \nKiabi\nBon \u00e9tat\n",
          "package_size_standard": true,
          "item_closing_action": null,
          "related_catalog_ids": [],
          "related_catalogs_enabled": false,
          "size": "S / 36 / 8",
          "brand": "Nike",
          "composition": "",
          "extra_conditions": "",
          "is_for_sell": true,
          "is_for_swap": false,
          "is_for_give_away": false,
          "is_handicraft": false,
          "is_draft": false,
          "label": "Nike",
          "real_value_numeric": null,
          "original_price_numeric": "6.0",
          "currency": "EUR",
          "price_numeric": "4.0",
          "created_at_ts": "2021-05-10T22:28:39+02:00",
          "updated_at_ts": "2021-05-20T18:11:57+02:00",
          "user_updated_at_ts": "2021-05-19T22:12:03+02:00",
          "photos": [
            {
              "id": 4008552810,
              "image_no": 1,
              "width": 370,
              "height": 800,
              "dominant_color": "#BFA2B0",
              "dominant_color_opaque": "#ECE3E7",
              "url": "https://images.vinted.net/thumbs/f800/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-581edff4fe4180816bd16f5a9b9c856677f37018",
              "is_main": true,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-f927fae6158aff3d559bc28b7cc1c5b56b1cf1b2",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-fc4d456e8e9da52a18841506acc9facc743c4fe8",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-80eabab162dcf13cc89c61bb90b2a97184acf3f2",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-581edff4fe4180816bd16f5a9b9c856677f37018",
                  "width": 197,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-581edff4fe4180816bd16f5a9b9c856677f37018",
                  "width": 288,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-581edff4fe4180816bd16f5a9b9c856677f37018",
                  "width": 168,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "03_02137_aCugnY4Qr9X1izrVPH5Tyb2S",
                "timestamp": 1620678519,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/03_02137_aCugnY4Qr9X1izrVPH5Tyb2S.jpeg?1620678519-eda50f9bf12b406cc5ef176ff1e18e66e8ee103c",
              "extra": {}
            },
            {
              "id": 4008552811,
              "image_no": 2,
              "width": 370,
              "height": 800,
              "dominant_color": "#827D7D",
              "dominant_color_opaque": "#DAD8D8",
              "url": "https://images.vinted.net/thumbs/f800/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-371caa6d7d4d39fdbcaa8f799dc6d9722bd3f4ca",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-c8899b9190feb8b068536f63864569793b157285",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-5d0b56be32c46ec0900ab4531ebd000d2d8b8cbf",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-df6045ae2586e6bed842b88eb023be58aeb011e0",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-371caa6d7d4d39fdbcaa8f799dc6d9722bd3f4ca",
                  "width": 197,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-371caa6d7d4d39fdbcaa8f799dc6d9722bd3f4ca",
                  "width": 288,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-371caa6d7d4d39fdbcaa8f799dc6d9722bd3f4ca",
                  "width": 168,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ",
                "timestamp": 1620678519,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/02_00ac8_d9zx2bQJMc2Ykcu1j9LawZLQ.jpeg?1620678519-9094195efa8b52ca02bf483a40ea65694559a2ff",
              "extra": {}
            },
            {
              "id": 4008552708,
              "image_no": 3,
              "width": 370,
              "height": 800,
              "dominant_color": "#B0A0A6",
              "dominant_color_opaque": "#E7E3E4",
              "url": "https://images.vinted.net/thumbs/f800/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-52862e7f10e029c2d0cfd7c3ddc6ca69fb179bdd",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-86581ed15761f68069fe095fc7fc3a668fee94e3",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-bee2818ab38a5c762d4dd77751faf302ac5798ed",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-87a4f6cbf75e26989fe71458004869eee3d53796",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-52862e7f10e029c2d0cfd7c3ddc6ca69fb179bdd",
                  "width": 197,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-52862e7f10e029c2d0cfd7c3ddc6ca69fb179bdd",
                  "width": 288,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-52862e7f10e029c2d0cfd7c3ddc6ca69fb179bdd",
                  "width": 168,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c",
                "timestamp": 1620678519,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/03_00ea1_9kFkgE6SaTRZHVtDBcGjCv7c.jpeg?1620678519-3865fa763d79dc4acac93101b01797ca8da79019",
              "extra": {}
            },
            {
              "id": 4008552790,
              "image_no": 4,
              "width": 370,
              "height": 800,
              "dominant_color": "#E74A7F",
              "dominant_color_opaque": "#F8C9D9",
              "url": "https://images.vinted.net/thumbs/f800/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-15b4cce20c23a1673e06b728f887ed8dadac11fc",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-f7212bddf1fd0ceb012f44f45475e777c695aa06",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-12b3c25e14e6237c540e1dc114731385979f9298",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-8d28d06d207dda7ce21b17b4512022752bbc5106",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-15b4cce20c23a1673e06b728f887ed8dadac11fc",
                  "width": 197,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-15b4cce20c23a1673e06b728f887ed8dadac11fc",
                  "width": 288,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-15b4cce20c23a1673e06b728f887ed8dadac11fc",
                  "width": 168,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "03_00f12_YDHpVU9NhEBCWiYLhK5jPutG",
                "timestamp": 1620678519,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/03_00f12_YDHpVU9NhEBCWiYLhK5jPutG.jpeg?1620678519-2288126defd9dc7c64ab18964d0ea6388516b71e",
              "extra": {}
            },
            {
              "id": 4008552722,
              "image_no": 5,
              "width": 370,
              "height": 800,
              "dominant_color": "#E54F83",
              "dominant_color_opaque": "#F7CADA",
              "url": "https://images.vinted.net/thumbs/f800/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-fab362c3cc412b4fa6201d6f0a644728381cd888",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-ca12fa910b4c1ac5348e896f9bbaafe9077ea957",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-344a1647fc560d825dede483e4d13a777a326a0b",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-975e2cddf5f7b5ada2bd5123edc92ad761bd8564",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-fab362c3cc412b4fa6201d6f0a644728381cd888",
                  "width": 197,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-fab362c3cc412b4fa6201d6f0a644728381cd888",
                  "width": 288,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-fab362c3cc412b4fa6201d6f0a644728381cd888",
                  "width": 168,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "01_02566_RFN9S1ygDEeXAedSxd8M4rWW",
                "timestamp": 1620678519,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/01_02566_RFN9S1ygDEeXAedSxd8M4rWW.jpeg?1620678519-bd832d86a7fcf35e2f73aaf5aec05c005c432eab",
              "extra": {}
            },
            {
              "id": 4008552836,
              "image_no": 6,
              "width": 370,
              "height": 800,
              "dominant_color": "#DE7B8C",
              "dominant_color_opaque": "#F5D7DD",
              "url": "https://images.vinted.net/thumbs/f800/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-e941719ae5c170d5fdd286771a1b6ba40281bcc0",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-c73dc7c60fa92f5f1c1580aa9983fa3b428fb0cc",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-c338e511ee7a3e9fec783af9fbd70905aa27204b",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-f1850bbb9ff961b14386e8e57f253a8008d0792a",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-e941719ae5c170d5fdd286771a1b6ba40281bcc0",
                  "width": 197,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-e941719ae5c170d5fdd286771a1b6ba40281bcc0",
                  "width": 288,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-e941719ae5c170d5fdd286771a1b6ba40281bcc0",
                  "width": 168,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "02_02613_AveGZ5bokWFfNbibFfz9yPUj",
                "timestamp": 1620678519,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/02_02613_AveGZ5bokWFfNbibFfz9yPUj.jpeg?1620678519-93156333e19222b6ab4e48e913fa17424ec653a4",
              "extra": {}
            }
          ],
          "push_up_interval": 604800,
          "can_be_sold": true,
          "can_feedback": false,
          "path": "/femmes/tee-shirts/1101845357-lot-t-shirt-taille-s",
          "possible_to_request_reservation": true,
          "item_reservation_id": null,
          "receiver_id": null,
          "promoted_until": "2021-05-22T22:12:03+02:00",
          "discount_price_numeric": null,
          "badge": null,
          "reservation_requests_from_users": [],
          "material_id": null,
          "author": null,
          "book_title": null,
          "isbn": null,
          "defect_ids": [],
          "user": {
            "id": 20178521,
            "anon_id": "1538b83a-9e3e-4a63-acc8-6c8d45b30dff",
            "login": "david-flo",
            "real_name": null,
            "email": null,
            "birthday": null,
            "gender": "M",
            "item_count": 48,
            "msg_template_count": 2,
            "given_item_count": 87,
            "taken_item_count": 0,
            "favourite_topic_count": 1,
            "forum_msg_count": 3,
            "forum_topic_count": 1,
            "followers_count": 18,
            "following_count": 23,
            "following_brands_count": 0,
            "positive_feedback_count": 40,
            "neutral_feedback_count": 1,
            "negative_feedback_count": 0,
            "meeting_transaction_count": 0,
            "account_status": 0,
            "email_bounces": null,
            "feedback_reputation": 0.976,
            "account_ban_date": null,
            "is_account_ban_permanent": null,
            "is_forum_ban_permanent": null,
            "is_on_holiday": false,
            "is_publish_photos_agreed": false,
            "is_shadow_banned": false,
            "is_identity": false,
            "expose_location": true,
            "third_party_tracking": true,
            "default_address": null,
            "created_at": "2018-11-27T18:38:43+01:00",
            "last_loged_on_ts": "2021-05-20T16:16:13+02:00",
            "city_id": 14928,
            "city": "Saint-Laurent-du-Var",
            "country_id": 16,
            "country_code": "FR",
            "country_iso_code": "FR",
            "country_title_local": "France",
            "country_title": "France",
            "contacts_permission": null,
            "contacts": null,
            "photo": {
              "id": 13162537,
              "width": 800,
              "height": 663,
              "temp_uuid": null,
              "url": "https://images.vinted.net/thumbs/f800/02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8.jpeg?1605221292-256f221b49976901478f9ac1690bae43d4feedf2",
              "dominant_color": "#31abc2",
              "dominant_color_opaque": "#C1E6ED",
              "thumbnails": [
                {
                  "type": "thumb310",
                  "url": "https://images.vinted.net/thumbs/310x310/02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8.jpeg?1605221292-89613c13e7b52a599551421f4052d7fe870e6e9f",
                  "width": 310,
                  "height": 310,
                  "original_size": null
                },
                {
                  "type": "thumb150",
                  "url": "https://images.vinted.net/thumbs/150x150/02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8.jpeg?1605221292-201c2096fc083c3f269b5122e621e28cf3eac7a2",
                  "width": 150,
                  "height": 150,
                  "original_size": null
                },
                {
                  "type": "thumb100",
                  "url": "https://images.vinted.net/thumbs/100x100/02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8.jpeg?1605221292-1b8e1c448306aca467e92a55f6c63a8806fcda00",
                  "width": 100,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb50",
                  "url": "https://images.vinted.net/thumbs/50x50/02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8.jpeg?1605221292-2651d0a33765a8b6d7e4288b8fbd0b305e47f707",
                  "width": 50,
                  "height": 50,
                  "original_size": null
                },
                {
                  "type": "thumb20",
                  "url": "https://images.vinted.net/thumbs/20x20/02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8.jpeg?1605221292-732add9dcc0bcd940780470d0a8682d3d6413421",
                  "width": 20,
                  "height": 20,
                  "original_size": null
                }
              ],
              "is_suspicious": false,
              "orientation": null,
              "high_resolution": {
                "id": "02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8",
                "timestamp": 1605221292,
                "orientation": null
              },
              "full_size_url": "https://images.vinted.net/thumbs/02_005e0_KUpCDc6eXHZ9NWCk4x6e8hN8.jpeg?1605221292-023e3c989f83d3c165ce48417ea88a1ebaf236a1",
              "extra": {}
            },
            "path": "/member/20178521-david-flo",
            "is_god": false,
            "is_tester": false,
            "moderator": false,
            "volunteer_moderator": false,
            "hide_feedback": false,
            "can_post_big_forum_photos": false,
            "allow_direct_messaging": true,
            "bundle_discount": {
              "id": 2215849,
              "user_id": 20178521,
              "enabled": true,
              "minimal_item_count": 2,
              "fraction": "0.1",
              "discounts": [
                {
                  "minimal_item_count": 2,
                  "fraction": "0.1"
                },
                {
                  "minimal_item_count": 3,
                  "fraction": "0.15"
                },
                {
                  "minimal_item_count": 5,
                  "fraction": "0.2"
                }
              ]
            },
            "donation_configuration": null,
            "business": false,
            "business_account": null,
            "total_items_count": 135,
            "about": "Grossr quantite de vetement de la layette \u00e0 v\u00eatements filles 16 ans. Garcon jusqu&#39;\u00e0 10 ans.\nChaussures, v\u00eatements hiver, \u00e9t\u00e9 tout y est. A vois de me poser des questions.\nTout n&#39;est pas en ligne mais \u00e7a viendra.",
            "verification": {
              "email": {
                "valid": true,
                "available": true
              },
              "facebook": {
                "valid": true,
                "verified_at": "2018-11-27T18:38:01+01:00",
                "available": true,
                "friend_count": 235
              },
              "google": {
                "valid": true,
                "verified_at": "2019-08-28T10:44:48+02:00",
                "available": true
              },
              "phone": {
                "valid": true,
                "verified_at": "2019-08-28T11:38:02+02:00",
                "available": true
              }
            },
            "closet_promoted_until": "2021-05-21T08:16:29+02:00",
            "avg_response_time": null,
            "carrier_ids": [
              20,
              27,
              50,
              54,
              59,
              4,
              9,
              10
            ],
            "carriers_without_custom_ids": [
              20,
              27,
              50,
              54,
              59,
              4
            ],
            "locale": "fr",
            "updated_on": 1621523356,
            "is_hated": false,
            "hates_you": false,
            "is_favourite": false,
            "profile_url": "https://www.vinted.fr/member/20178521-david-flo",
            "facebook_user_id": null,
            "is_online": false,
            "has_promoted_closet": true,
            "can_view_profile": true,
            "can_bundle": true,
            "last_loged_on": "aujourd'hui 16:16",
            "accepted_pay_in_methods": [
              {
                "id": 1,
                "code": "CREDIT_CARD",
                "requires_credit_card": true,
                "event_tracking_code": "cc",
                "icon": "credit-card",
                "enabled": true,
                "translated_name": "Carte bancaire",
                "note": "Les informations li\u00e9es \u00e0 ta carte bancaire ne seront pas partag\u00e9es avec le vendeur. Vinted n'enregistre pas tes informations bancaires sans ton autorisation."
              },
              {
                "id": 4,
                "code": "SOFORT",
                "requires_credit_card": false,
                "event_tracking_code": "sofort",
                "icon": "sofort",
                "enabled": true,
                "translated_name": "Sofort",
                "note": ""
              },
              {
                "id": 16,
                "code": "APPLE_PAY",
                "requires_credit_card": false,
                "event_tracking_code": "apple_pay",
                "icon": "apple-pay",
                "enabled": true,
                "translated_name": "Apple Pay",
                "note": ""
              },
              {
                "id": 10,
                "code": "MANGOPAY_PAYPAL",
                "requires_credit_card": false,
                "event_tracking_code": "mangopay_paypal",
                "icon": "paypal",
                "enabled": true,
                "translated_name": "PayPal",
                "note": ""
              },
              {
                "id": 9,
                "code": "IDEAL",
                "requires_credit_card": false,
                "event_tracking_code": "ideal",
                "icon": "ideal",
                "enabled": true,
                "translated_name": "iDeal",
                "note": ""
              }
            ],
            "localization": "manual"
          },
          "price": "4,00 \u20ac",
          "discount_price": "",
          "real_value": "",
          "can_edit": false,
          "can_delete": false,
          "can_request_reservation": false,
          "can_cancel_reservation_request": false,
          "can_reserve": false,
          "can_transfer": false,
          "instant_buy": true,
          "can_close": false,
          "can_buy": true,
          "can_bundle": true,
          "can_ask_seller": true,
          "can_favourite": false,
          "user_login": "david-flo",
          "city_id": 14928,
          "city": "Saint-Laurent-du-Var",
          "country": "France",
          "nearby": null,
          "distance": null,
          "promoted": true,
          "is_favourite": false,
          "is_mobile": false,
          "bump_badge_visible": false,
          "brand_dto": {
            "id": 53,
            "title": "Nike",
            "slug": "nike",
            "favourite_count": 2859325,
            "pretty_favourite_count": "2.9M",
            "item_count": 10314076,
            "pretty_item_count": "10.3M",
            "is_visible_in_listings": true,
            "path": "/brand/nike",
            "requires_authenticity_check": true,
            "is_luxury": true,
            "url": "https://www.vinted.fr/brand/nike",
            "is_favourite": false,
            "is_hated": false
          },
          "url": "https://www.vinted.fr/femmes/tee-shirts/1101845357-lot-t-shirt-taille-s",
          "accepted_pay_in_methods": [
            {
              "id": 1,
              "code": "CREDIT_CARD",
              "requires_credit_card": true,
              "event_tracking_code": "cc",
              "icon": "credit-card",
              "enabled": true,
              "translated_name": "Carte bancaire",
              "note": "Les informations li\u00e9es \u00e0 ta carte bancaire ne seront pas partag\u00e9es avec le vendeur. Vinted n'enregistre pas tes informations bancaires sans ton autorisation."
            },
            {
              "id": 10,
              "code": "MANGOPAY_PAYPAL",
              "requires_credit_card": false,
              "event_tracking_code": "mangopay_paypal",
              "icon": "paypal",
              "enabled": true,
              "translated_name": "PayPal",
              "note": ""
            }
          ],
          "created_at": "10/05 22:28",
          "color1": "Rose",
          "color2": null,
          "material": null,
          "status": "Bon \u00e9tat",
          "secure_purchase": true,
          "performance": null,
          "stats_visible": true,
          "can_push_up": false,
          "size_guide_faq_entry_id": 506,
          "localization": "manual"
        },
        "1122074341": {
          "id": 1122074341,
          "title": "Camiseta Nike TXL ",
          "brand_id": 53,
          "size_id": 7,
          "status_id": 2,
          "disposal_conditions": 4,
          "user_id": 28918083,
          "owner_id": null,
          "country_id": 7,
          "catalog_id": 221,
          "color1_id": 3,
          "color2_id": 5,
          "package_size_id": 1,
          "is_hidden": 0,
          "is_reserved": 0,
          "reserved_for_user_id": null,
          "is_visible": 1,
          "is_unisex": 0,
          "is_closed": 0,
          "is_admin_alerted": false,
          "active_bid_count": 1,
          "favourite_count": 1,
          "view_count": 5,
          "moderation_status": 0,
          "last_push_up_at": "2021-05-19T20:58:42+02:00",
          "description": "Larga ",
          "package_size_standard": true,
          "item_closing_action": null,
          "related_catalog_ids": [],
          "related_catalogs_enabled": false,
          "size": "XXL / 44 / 16",
          "brand": "Nike",
          "composition": "",
          "extra_conditions": "",
          "is_for_sell": true,
          "is_for_swap": false,
          "is_for_give_away": false,
          "is_handicraft": false,
          "is_draft": false,
          "label": "Nike",
          "real_value_numeric": null,
          "original_price_numeric": "8.0",
          "currency": "EUR",
          "price_numeric": "8.0",
          "created_at_ts": "2021-05-19T20:58:42+02:00",
          "updated_at_ts": "2021-05-20T12:57:44+02:00",
          "user_updated_at_ts": "2021-05-19T20:58:42+02:00",
          "photos": [
            {
              "id": 4089680228,
              "image_no": 1,
              "width": 600,
              "height": 800,
              "dominant_color": "#5D544A",
              "dominant_color_opaque": "#CECCC9",
              "url": "https://images.vinted.net/thumbs/f800/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-89880edaf27b5cb7aa5d5f82ca1175b2a8e54d62",
              "is_main": true,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-96d62d346e94e220a705d8f75dd0a84518497758",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-4c33a479637c9322c871742001f9cac562806052",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-676a351d5f82c40a6284a50e8fc5e3e13fa66792",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-89880edaf27b5cb7aa5d5f82ca1175b2a8e54d62",
                  "width": 321,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-89880edaf27b5cb7aa5d5f82ca1175b2a8e54d62",
                  "width": 468,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-89880edaf27b5cb7aa5d5f82ca1175b2a8e54d62",
                  "width": 273,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2",
                "timestamp": 1621450722,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/03_01b89_FEwtmgZTuQ7eEWapVvuHy5Z2.jpeg?1621450722-348b62b74b98564b7f74b2b9760a2c6807155aff",
              "extra": {}
            },
            {
              "id": 4089680380,
              "image_no": 2,
              "width": 600,
              "height": 800,
              "dominant_color": "#675A49",
              "dominant_color_opaque": "#D1CEC8",
              "url": "https://images.vinted.net/thumbs/f800/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-b82f96b778db1b1d4cd2b58b95fc8945fd0fffbe",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-8dc9035b540466e81134cfd21006769d43ed6b93",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-5be88665a81044f026f2509100af42f5f86f1976",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-ea1bdb2b62c05ae5080a742adddfdda9d6478a89",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-b82f96b778db1b1d4cd2b58b95fc8945fd0fffbe",
                  "width": 321,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-b82f96b778db1b1d4cd2b58b95fc8945fd0fffbe",
                  "width": 468,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-b82f96b778db1b1d4cd2b58b95fc8945fd0fffbe",
                  "width": 273,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "03_00cba_TiBriFEZ8LHqJpps9mL46tZY",
                "timestamp": 1621450722,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/03_00cba_TiBriFEZ8LHqJpps9mL46tZY.jpeg?1621450722-1a9cd2d08ec9fe40d2642045a4fea139d17a38cf",
              "extra": {}
            },
            {
              "id": 4089680499,
              "image_no": 3,
              "width": 800,
              "height": 600,
              "dominant_color": "#754C46",
              "dominant_color_opaque": "#D6C9C8",
              "url": "https://images.vinted.net/thumbs/f800/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-7a5cbea2b7284501d6526ac5b263ef299eb6a5b1",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-2cefaef812bdba508436b04381174c115092775e",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-fd058a9efa4a77183b3a456e76b0ca619b61b6b1",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-4e11c47e651386402dd4015ed824ba8b0790b4d6",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-7a5cbea2b7284501d6526ac5b263ef299eb6a5b1",
                  "width": 428,
                  "height": 321,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-7a5cbea2b7284501d6526ac5b263ef299eb6a5b1",
                  "width": 624,
                  "height": 468,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-7a5cbea2b7284501d6526ac5b263ef299eb6a5b1",
                  "width": 364,
                  "height": 273,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "03_01356_V8qiQR5Kun6JM7kFjdX745rS",
                "timestamp": 1621450722,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/03_01356_V8qiQR5Kun6JM7kFjdX745rS.jpeg?1621450722-5abe39b2827587f37b5ccc3d14aa0b163952596e",
              "extra": {}
            }
          ],
          "push_up_interval": 604800,
          "can_be_sold": true,
          "can_feedback": false,
          "path": "/femmes/tee-shirts/1122074341-camiseta-nike-txl",
          "possible_to_request_reservation": true,
          "item_reservation_id": null,
          "receiver_id": null,
          "promoted_until": null,
          "discount_price_numeric": null,
          "badge": null,
          "reservation_requests_from_users": [],
          "material_id": null,
          "author": null,
          "book_title": null,
          "isbn": null,
          "defect_ids": [],
          "user": {
            "id": 28918083,
            "anon_id": "1e2b71af-90b6-48f7-b05a-7f46bf28642e",
            "login": "rominamalaga",
            "real_name": null,
            "email": null,
            "birthday": null,
            "gender": "F",
            "item_count": 140,
            "msg_template_count": 6,
            "given_item_count": 223,
            "taken_item_count": 152,
            "favourite_topic_count": 0,
            "forum_msg_count": 0,
            "forum_topic_count": 0,
            "followers_count": 60,
            "following_count": 7,
            "following_brands_count": 7,
            "positive_feedback_count": 230,
            "neutral_feedback_count": 7,
            "negative_feedback_count": 37,
            "meeting_transaction_count": 0,
            "account_status": 0,
            "email_bounces": null,
            "feedback_reputation": 0.876,
            "account_ban_date": null,
            "is_account_ban_permanent": null,
            "is_forum_ban_permanent": null,
            "is_on_holiday": false,
            "is_publish_photos_agreed": false,
            "is_shadow_banned": false,
            "is_identity": false,
            "expose_location": true,
            "third_party_tracking": true,
            "default_address": null,
            "created_at": "2019-09-25T19:20:35+02:00",
            "last_loged_on_ts": "2021-05-20T20:12:56+02:00",
            "city_id": 88320,
            "city": "Malaga",
            "country_id": 7,
            "country_code": "ES",
            "country_iso_code": "ES",
            "country_title_local": "Espa\u00f1a",
            "country_title": "Espa\u00f1a",
            "contacts_permission": null,
            "contacts": null,
            "photo": {
              "id": 21726200,
              "width": 640,
              "height": 799,
              "temp_uuid": null,
              "url": "https://images.vinted.net/thumbs/f800/02_00867_26MfZ5TogDV6potbNtMKZtuc.jpeg?1605226339-7d14090087852a75e1cc5cd380d5fa02c91eaf72",
              "dominant_color": "#31abc2",
              "dominant_color_opaque": "#C1E6ED",
              "thumbnails": [
                {
                  "type": "thumb310",
                  "url": "https://images.vinted.net/thumbs/310x310/02_00867_26MfZ5TogDV6potbNtMKZtuc.jpeg?1605226339-fdb52237ababbec1207c319ed447616ee9a1eb3a",
                  "width": 310,
                  "height": 310,
                  "original_size": null
                },
                {
                  "type": "thumb150",
                  "url": "https://images.vinted.net/thumbs/150x150/02_00867_26MfZ5TogDV6potbNtMKZtuc.jpeg?1605226339-471b73e7029fc2af3be5d8728d33bf74a7b6fd8c",
                  "width": 150,
                  "height": 150,
                  "original_size": null
                },
                {
                  "type": "thumb100",
                  "url": "https://images.vinted.net/thumbs/100x100/02_00867_26MfZ5TogDV6potbNtMKZtuc.jpeg?1605226339-fabaac3505d4808ec5324ff301e8f1f44a3d9c22",
                  "width": 100,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb50",
                  "url": "https://images.vinted.net/thumbs/50x50/02_00867_26MfZ5TogDV6potbNtMKZtuc.jpeg?1605226339-e332e6c4850828c4663974173a5e87ca21dd13ac",
                  "width": 50,
                  "height": 50,
                  "original_size": null
                },
                {
                  "type": "thumb20",
                  "url": "https://images.vinted.net/thumbs/20x20/02_00867_26MfZ5TogDV6potbNtMKZtuc.jpeg?1605226339-235fc1b65cd9853f8bd2d8fbf14e74bb97c1531a",
                  "width": 20,
                  "height": 20,
                  "original_size": null
                }
              ],
              "is_suspicious": false,
              "orientation": null,
              "high_resolution": {
                "id": "02_00867_26MfZ5TogDV6potbNtMKZtuc",
                "timestamp": 1605226339,
                "orientation": null
              },
              "full_size_url": "https://images.vinted.net/thumbs/02_00867_26MfZ5TogDV6potbNtMKZtuc.jpeg?1605226339-ee40ea9d9344390f98441413fbbf9d30cbfa9049",
              "extra": {}
            },
            "path": "/member/28918083-rominamalaga",
            "is_god": false,
            "is_tester": false,
            "moderator": false,
            "volunteer_moderator": false,
            "hide_feedback": false,
            "can_post_big_forum_photos": false,
            "allow_direct_messaging": true,
            "bundle_discount": {
              "id": 4202659,
              "user_id": 28918083,
              "enabled": false,
              "minimal_item_count": 2,
              "fraction": "0.05",
              "discounts": [
                {
                  "minimal_item_count": 2,
                  "fraction": "0.05"
                },
                {
                  "minimal_item_count": 3,
                  "fraction": "0.05"
                },
                {
                  "minimal_item_count": 5,
                  "fraction": "0.05"
                }
              ]
            },
            "donation_configuration": null,
            "business": false,
            "business_account": null,
            "total_items_count": 363,
            "about": "",
            "verification": {
              "email": {
                "valid": true,
                "available": true
              },
              "facebook": {
                "valid": false,
                "verified_at": null,
                "available": true,
                "friend_count": null
              },
              "google": {
                "valid": false,
                "verified_at": null,
                "available": true
              },
              "phone": {
                "valid": true,
                "verified_at": "2019-09-25T19:26:02+02:00",
                "available": true
              }
            },
            "closet_promoted_until": null,
            "avg_response_time": null,
            "carrier_ids": [
              11,
              33,
              34,
              36,
              44,
              55,
              4,
              9,
              10
            ],
            "carriers_without_custom_ids": [
              11,
              33,
              34,
              36,
              44,
              55,
              4
            ],
            "locale": "es-fr",
            "updated_on": 1621515592,
            "is_hated": false,
            "hates_you": false,
            "is_favourite": false,
            "profile_url": "https://www.vinted.fr/member/28918083-rominamalaga",
            "facebook_user_id": null,
            "is_online": false,
            "has_promoted_closet": false,
            "can_view_profile": true,
            "can_bundle": true,
            "last_loged_on": "aujourd'hui 20:12",
            "accepted_pay_in_methods": [
              {
                "id": 1,
                "code": "CREDIT_CARD",
                "requires_credit_card": true,
                "event_tracking_code": "cc",
                "icon": "credit-card",
                "enabled": true,
                "translated_name": "Carte bancaire",
                "note": "Les informations li\u00e9es \u00e0 ta carte bancaire ne seront pas partag\u00e9es avec le vendeur. Vinted n'enregistre pas tes informations bancaires sans ton autorisation."
              },
              {
                "id": 4,
                "code": "SOFORT",
                "requires_credit_card": false,
                "event_tracking_code": "sofort",
                "icon": "sofort",
                "enabled": true,
                "translated_name": "Sofort",
                "note": ""
              },
              {
                "id": 16,
                "code": "APPLE_PAY",
                "requires_credit_card": false,
                "event_tracking_code": "apple_pay",
                "icon": "apple-pay",
                "enabled": true,
                "translated_name": "Apple Pay",
                "note": ""
              },
              {
                "id": 10,
                "code": "MANGOPAY_PAYPAL",
                "requires_credit_card": false,
                "event_tracking_code": "mangopay_paypal",
                "icon": "paypal",
                "enabled": true,
                "translated_name": "PayPal",
                "note": ""
              },
              {
                "id": 9,
                "code": "IDEAL",
                "requires_credit_card": false,
                "event_tracking_code": "ideal",
                "icon": "ideal",
                "enabled": true,
                "translated_name": "iDeal",
                "note": ""
              }
            ],
            "localization": "manual"
          },
          "price": "8,00 \u20ac",
          "discount_price": "",
          "real_value": "",
          "can_edit": false,
          "can_delete": false,
          "can_request_reservation": false,
          "can_cancel_reservation_request": false,
          "can_reserve": false,
          "can_transfer": false,
          "instant_buy": true,
          "can_close": false,
          "can_buy": true,
          "can_bundle": true,
          "can_ask_seller": true,
          "can_favourite": false,
          "user_login": "rominamalaga",
          "city_id": 88320,
          "city": "Malaga",
          "country": "Espa\u00f1a",
          "nearby": null,
          "distance": null,
          "promoted": false,
          "is_favourite": false,
          "is_mobile": false,
          "bump_badge_visible": false,
          "brand_dto": {
            "id": 53,
            "title": "Nike",
            "slug": "nike",
            "favourite_count": 2859325,
            "pretty_favourite_count": "2.9M",
            "item_count": 10314076,
            "pretty_item_count": "10.3M",
            "is_visible_in_listings": true,
            "path": "/brand/nike",
            "requires_authenticity_check": true,
            "is_luxury": true,
            "url": "https://www.vinted.fr/brand/nike",
            "is_favourite": false,
            "is_hated": false
          },
          "url": "https://www.vinted.fr/femmes/tee-shirts/1122074341-camiseta-nike-txl",
          "accepted_pay_in_methods": [
            {
              "id": 1,
              "code": "CREDIT_CARD",
              "requires_credit_card": true,
              "event_tracking_code": "cc",
              "icon": "credit-card",
              "enabled": true,
              "translated_name": "Carte bancaire",
              "note": "Les informations li\u00e9es \u00e0 ta carte bancaire ne seront pas partag\u00e9es avec le vendeur. Vinted n'enregistre pas tes informations bancaires sans ton autorisation."
            },
            {
              "id": 10,
              "code": "MANGOPAY_PAYPAL",
              "requires_credit_card": false,
              "event_tracking_code": "mangopay_paypal",
              "icon": "paypal",
              "enabled": true,
              "translated_name": "PayPal",
              "note": ""
            }
          ],
          "created_at": "hier 20:58",
          "color1": "Gris",
          "color2": "Rose",
          "material": null,
          "status": "Tr\u00e8s bon \u00e9tat",
          "secure_purchase": true,
          "performance": null,
          "stats_visible": false,
          "can_push_up": false,
          "size_guide_faq_entry_id": 506,
          "localization": "manual"
        },
        "1123689042": {
          "id": 1123689042,
          "title": "tee-shirts Nike manche 3/4",
          "brand_id": 53,
          "size_id": 4,
          "status_id": 1,
          "disposal_conditions": 4,
          "user_id": 14274668,
          "owner_id": null,
          "country_id": 16,
          "catalog_id": 221,
          "color1_id": 5,
          "color2_id": 6,
          "package_size_id": 1,
          "is_hidden": 0,
          "is_reserved": 0,
          "reserved_for_user_id": null,
          "is_visible": 1,
          "is_unisex": 0,
          "is_closed": 0,
          "is_admin_alerted": false,
          "active_bid_count": 0,
          "favourite_count": 0,
          "view_count": 0,
          "moderation_status": 0,
          "last_push_up_at": "2021-05-20T19:56:17+02:00",
          "description": "tee-shirts Nike neuf ",
          "package_size_standard": true,
          "item_closing_action": null,
          "related_catalog_ids": [],
          "related_catalogs_enabled": false,
          "size": "M / 38 / 10",
          "brand": "Nike",
          "composition": "",
          "extra_conditions": "",
          "is_for_sell": true,
          "is_for_swap": false,
          "is_for_give_away": false,
          "is_handicraft": false,
          "is_draft": false,
          "label": "Nike",
          "real_value_numeric": null,
          "original_price_numeric": "5.0",
          "currency": "EUR",
          "price_numeric": "5.0",
          "created_at_ts": "2021-05-20T19:56:17+02:00",
          "updated_at_ts": "2021-05-20T19:56:17+02:00",
          "user_updated_at_ts": "2021-05-20T19:56:17+02:00",
          "photos": [
            {
              "id": 4096278243,
              "image_no": 1,
              "width": 450,
              "height": 800,
              "dominant_color": "#850D33",
              "dominant_color_opaque": "#DAB6C2",
              "url": "https://images.vinted.net/thumbs/f800/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-0d0f4a4915e6871eba42e08f27a763d7c411a6db",
              "is_main": true,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-e769cfaea435375a390ac02fa05deacce837adb9",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-72f77727446c36ca48ef83cae544183cbd2da005",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-bc2d82dbaa4d03fb870c11e51ab5f144beec7799",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-0d0f4a4915e6871eba42e08f27a763d7c411a6db",
                  "width": 240,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-0d0f4a4915e6871eba42e08f27a763d7c411a6db",
                  "width": 351,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-0d0f4a4915e6871eba42e08f27a763d7c411a6db",
                  "width": 204,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX",
                "timestamp": 1621533377,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/02_00ab0_Pw9Jqhum4bbWk7CRLfwS3MZX.jpeg?1621533377-f242c588e492f0c4c655245d00bd89b27751d68a",
              "extra": {}
            },
            {
              "id": 4096282718,
              "image_no": 2,
              "width": 450,
              "height": 800,
              "dominant_color": "#AA2746",
              "dominant_color_opaque": "#E6BEC8",
              "url": "https://images.vinted.net/thumbs/f800/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-60a49f30e553bbf8132bea9f8588104b4a9ef39c",
              "is_main": false,
              "thumbnails": [
                {
                  "type": "thumb70x100",
                  "url": "https://images.vinted.net/thumbs/70x100/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-f06bd66a5b7107b50eaa2ea7557fa2dd04173f3d",
                  "width": 70,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb150x210",
                  "url": "https://images.vinted.net/thumbs/150x210/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-1ebb93182fe1126a47709351078ec78f6918e889",
                  "width": 150,
                  "height": 210,
                  "original_size": null
                },
                {
                  "type": "thumb310x430",
                  "url": "https://images.vinted.net/thumbs/310x430/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-1dace110e5f44d87b52086c06483888485e497d1",
                  "width": 310,
                  "height": 430,
                  "original_size": null
                },
                {
                  "type": "thumb428x624",
                  "url": "https://images.vinted.net/thumbs/f800/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-60a49f30e553bbf8132bea9f8588104b4a9ef39c",
                  "width": 240,
                  "height": 428,
                  "original_size": true
                },
                {
                  "type": "thumb624x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-60a49f30e553bbf8132bea9f8588104b4a9ef39c",
                  "width": 351,
                  "height": 624,
                  "original_size": true
                },
                {
                  "type": "thumb364x428",
                  "url": "https://images.vinted.net/thumbs/f800/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-60a49f30e553bbf8132bea9f8588104b4a9ef39c",
                  "width": 204,
                  "height": 364,
                  "original_size": true
                }
              ],
              "high_resolution": {
                "id": "03_01631_sdPGF9do7cuhTeuywXd41tey",
                "timestamp": 1621533377,
                "orientation": null
              },
              "is_suspicious": false,
              "full_size_url": "https://images.vinted.net/thumbs/03_01631_sdPGF9do7cuhTeuywXd41tey.jpeg?1621533377-691a663026f66194511df656bad2c73150fb8ecd",
              "extra": {}
            }
          ],
          "push_up_interval": 604800,
          "can_be_sold": true,
          "can_feedback": false,
          "path": "/femmes/tee-shirts/1123689042-tee-shirts-nike-manche-34",
          "possible_to_request_reservation": true,
          "item_reservation_id": null,
          "receiver_id": null,
          "promoted_until": null,
          "discount_price_numeric": null,
          "badge": null,
          "reservation_requests_from_users": [],
          "material_id": null,
          "author": null,
          "book_title": null,
          "isbn": null,
          "defect_ids": [],
          "user": {
            "id": 14274668,
            "anon_id": "1f57a9b1-7f55-49b3-8767-416514e85e98",
            "login": "romanegiry",
            "real_name": null,
            "email": null,
            "birthday": null,
            "gender": "F",
            "item_count": 28,
            "msg_template_count": 0,
            "given_item_count": 7,
            "taken_item_count": 19,
            "favourite_topic_count": 0,
            "forum_msg_count": 0,
            "forum_topic_count": 0,
            "followers_count": 5,
            "following_count": 15,
            "following_brands_count": 13,
            "positive_feedback_count": 12,
            "neutral_feedback_count": 0,
            "negative_feedback_count": 1,
            "meeting_transaction_count": 0,
            "account_status": 0,
            "email_bounces": null,
            "feedback_reputation": 0.954,
            "account_ban_date": null,
            "is_account_ban_permanent": null,
            "is_forum_ban_permanent": null,
            "is_on_holiday": false,
            "is_publish_photos_agreed": true,
            "is_shadow_banned": false,
            "is_identity": false,
            "expose_location": true,
            "third_party_tracking": true,
            "default_address": null,
            "created_at": "2017-10-21T13:34:04+02:00",
            "last_loged_on_ts": "2021-05-20T19:06:36+02:00",
            "city_id": null,
            "city": "",
            "country_id": 16,
            "country_code": "FR",
            "country_iso_code": "FR",
            "country_title_local": "France",
            "country_title": "France",
            "contacts_permission": null,
            "contacts": null,
            "photo": {
              "id": 29570237,
              "width": 600,
              "height": 800,
              "temp_uuid": null,
              "url": "https://images.vinted.net/thumbs/f800/02_022da_7427dTW2ZMNyiXSaKKPqBjtb.jpeg?1605251217-eb67b407074e9c4e7bf381bbe2ccca65d693d00a",
              "dominant_color": "#31abc2",
              "dominant_color_opaque": "#C1E6ED",
              "thumbnails": [
                {
                  "type": "thumb310",
                  "url": "https://images.vinted.net/thumbs/310x310/02_022da_7427dTW2ZMNyiXSaKKPqBjtb.jpeg?1605251217-68415f7b041483979ff2f4545f4c841c99405a69",
                  "width": 310,
                  "height": 310,
                  "original_size": null
                },
                {
                  "type": "thumb150",
                  "url": "https://images.vinted.net/thumbs/150x150/02_022da_7427dTW2ZMNyiXSaKKPqBjtb.jpeg?1605251217-f690a7dc0af0dac6944f1b575ccc1030fc42d4d4",
                  "width": 150,
                  "height": 150,
                  "original_size": null
                },
                {
                  "type": "thumb100",
                  "url": "https://images.vinted.net/thumbs/100x100/02_022da_7427dTW2ZMNyiXSaKKPqBjtb.jpeg?1605251217-3e287f3d2622b6c818c8006941e7e184b936346b",
                  "width": 100,
                  "height": 100,
                  "original_size": null
                },
                {
                  "type": "thumb50",
                  "url": "https://images.vinted.net/thumbs/50x50/02_022da_7427dTW2ZMNyiXSaKKPqBjtb.jpeg?1605251217-bf0526289dca76a29f486250bf02f1f789736d1c",
                  "width": 50,
                  "height": 50,
                  "original_size": null
                },
                {
                  "type": "thumb20",
                  "url": "https://images.vinted.net/thumbs/20x20/02_022da_7427dTW2ZMNyiXSaKKPqBjtb.jpeg?1605251217-da20b96495b0dcb250659c46ccfb5087bf3e6aea",
                  "width": 20,
                  "height": 20,
                  "original_size": null
                }
              ],
              "is_suspicious": false,
              "orientation": null,
              "high_resolution": {
                "id": "02_022da_7427dTW2ZMNyiXSaKKPqBjtb",
                "timestamp": 1605251217,
                "orientation": null
              },
              "full_size_url": "https://images.vinted.net/thumbs/02_022da_7427dTW2ZMNyiXSaKKPqBjtb.jpeg?1605251217-cbbab139cb38befc5bed0690e3af6acbfd1ce99c",
              "extra": {}
            },
            "path": "/member/14274668-romanegiry",
            "is_god": false,
            "is_tester": false,
            "moderator": false,
            "volunteer_moderator": false,
            "hide_feedback": false,
            "can_post_big_forum_photos": false,
            "allow_direct_messaging": true,
            "bundle_discount": {
              "id": 3770689,
              "user_id": 14274668,
              "enabled": true,
              "minimal_item_count": 2,
              "fraction": "0.2",
              "discounts": [
                {
                  "minimal_item_count": 2,
                  "fraction": "0.2"
                },
                {
                  "minimal_item_count": 3,
                  "fraction": "0.25"
                },
                {
                  "minimal_item_count": 5,
                  "fraction": "0.3"
                }
              ]
            },
            "donation_configuration": null,
            "business": false,
            "business_account": null,
            "total_items_count": 35,
            "about": "",
            "verification": {
              "email": {
                "valid": true,
                "available": true
              },
              "facebook": {
                "valid": false,
                "verified_at": null,
                "available": true,
                "friend_count": null
              },
              "google": {
                "valid": true,
                "verified_at": "2017-10-21T13:33:50+02:00",
                "available": true
              },
              "phone": {
                "valid": false,
                "verified_at": null,
                "available": true
              }
            },
            "closet_promoted_until": null,
            "avg_response_time": null,
            "carrier_ids": [
              20,
              27,
              50,
              54,
              59,
              4,
              9,
              10
            ],
            "carriers_without_custom_ids": [
              20,
              27,
              50,
              54,
              59,
              4
            ],
            "locale": "fr",
            "updated_on": 1621533976,
            "is_hated": false,
            "hates_you": false,
            "is_favourite": false,
            "profile_url": "https://www.vinted.fr/member/14274668-romanegiry",
            "facebook_user_id": null,
            "is_online": false,
            "has_promoted_closet": false,
            "can_view_profile": true,
            "can_bundle": true,
            "last_loged_on": "aujourd'hui 19:06",
            "accepted_pay_in_methods": [
              {
                "id": 1,
                "code": "CREDIT_CARD",
                "requires_credit_card": true,
                "event_tracking_code": "cc",
                "icon": "credit-card",
                "enabled": true,
                "translated_name": "Carte bancaire",
                "note": "Les informations li\u00e9es \u00e0 ta carte bancaire ne seront pas partag\u00e9es avec le vendeur. Vinted n'enregistre pas tes informations bancaires sans ton autorisation."
              },
              {
                "id": 4,
                "code": "SOFORT",
                "requires_credit_card": false,
                "event_tracking_code": "sofort",
                "icon": "sofort",
                "enabled": true,
                "translated_name": "Sofort",
                "note": ""
              },
              {
                "id": 16,
                "code": "APPLE_PAY",
                "requires_credit_card": false,
                "event_tracking_code": "apple_pay",
                "icon": "apple-pay",
                "enabled": true,
                "translated_name": "Apple Pay",
                "note": ""
              },
              {
                "id": 10,
                "code": "MANGOPAY_PAYPAL",
                "requires_credit_card": false,
                "event_tracking_code": "mangopay_paypal",
                "icon": "paypal",
                "enabled": true,
                "translated_name": "PayPal",
                "note": ""
              },
              {
                "id": 9,
                "code": "IDEAL",
                "requires_credit_card": false,
                "event_tracking_code": "ideal",
                "icon": "ideal",
                "enabled": true,
                "translated_name": "iDeal",
                "note": ""
              }
            ],
            "localization": "manual"
          },
          "price": "5,00 \u20ac",
          "discount_price": "",
          "real_value": "",
          "can_edit": false,
          "can_delete": false,
          "can_request_reservation": false,
          "can_cancel_reservation_request": false,
          "can_reserve": false,
          "can_transfer": false,
          "instant_buy": true,
          "can_close": false,
          "can_buy": true,
          "can_bundle": true,
          "can_ask_seller": true,
          "can_favourite": false,
          "user_login": "romanegiry",
          "city_id": null,
          "city": "",
          "country": "France",
          "nearby": null,
          "distance": null,
          "promoted": false,
          "is_favourite": false,
          "is_mobile": false,
          "bump_badge_visible": false,
          "brand_dto": {
            "id": 53,
            "title": "Nike",
            "slug": "nike",
            "favourite_count": 2859325,
            "pretty_favourite_count": "2.9M",
            "item_count": 10314076,
            "pretty_item_count": "10.3M",
            "is_visible_in_listings": true,
            "path": "/brand/nike",
            "requires_authenticity_check": true,
            "is_luxury": true,
            "url": "https://www.vinted.fr/brand/nike",
            "is_favourite": false,
            "is_hated": false
          },
          "url": "https://www.vinted.fr/femmes/tee-shirts/1123689042-tee-shirts-nike-manche-34",
          "accepted_pay_in_methods": [
            {
              "id": 1,
              "code": "CREDIT_CARD",
              "requires_credit_card": true,
              "event_tracking_code": "cc",
              "icon": "credit-card",
              "enabled": true,
              "translated_name": "Carte bancaire",
              "note": "Les informations li\u00e9es \u00e0 ta carte bancaire ne seront pas partag\u00e9es avec le vendeur. Vinted n'enregistre pas tes informations bancaires sans ton autorisation."
            },
            {
              "id": 10,
              "code": "MANGOPAY_PAYPAL",
              "requires_credit_card": false,
              "event_tracking_code": "mangopay_paypal",
              "icon": "paypal",
              "enabled": true,
              "translated_name": "PayPal",
              "note": ""
            }
          ],
          "created_at": "aujourd'hui 19:56",
          "color1": "Rose",
          "color2": "Violet",
          "material": null,
          "status": "Neuf sans \u00e9tiquette",
          "secure_purchase": true,
          "performance": null,
          "stats_visible": false,
          "can_push_up": false,
          "size_guide_faq_entry_id": 506,
          "localization": "manual"
        }
      },
      "searchParams": {
        "ids": [
          1101845357,
          1122074341,
          1123689042
        ],
        "searchParams": {
          "1101845357": {
            "score": 5.1769934,
            "matched_queries": null
          },
          "1122074341": {
            "score": 3.5682194,
            "matched_queries": null
          },
          "1123689042": {
            "score": 3.5542152,
            "matched_queries": null
          }
        },
        "uiState": "IDLE",
        "errors": null,
        "currentPage": 1,
        "totalPages": 32,
        "totalEntries": 3000,
        "perPage": 96,
        "time": 1621536628,
        "endReached": false
      }
    }
  ```
</details>



