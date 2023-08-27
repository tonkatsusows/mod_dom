#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl as op
import json

wb=op.load_workbook("mod.xlsx")
ws=wb['item_only']

def block_state(item_id):
    result=["{",'   "variants":{','   "":{','       "model":"cbs:block/'+item_id+'"','      }','   }','}']

    txt=""
    for x in result:
        txt=txt+x+"\n"

    text=json.loads(txt)

    file_name="bs/"+item_id+".json"
    with open(file_name,'w') as f:
        json.dump(text,f,indent=4)

def item_model(item_id):
    result=["{",'   "parent":"minecraft:item/generated",','   "textures":{','       "layer0":"cbs:item/'+item_id+'"','   }','}']

    txt=""
    for x in result:
        txt=txt+x+"\n"

    text=json.loads(txt)

    file_name="model/item/"+item_id+".json"
    with open(file_name,'w') as f:
        json.dump(text,f,indent=4)

def block_model(item_id):
    result=["{",'   "parent":"minecraft:block/cube_all",','   "textures":{','       "all":"cbs:block/'+item_id+'"','   }','}']

    txt=""
    for x in result:
        txt=txt+x+"\n"

    text=json.loads(txt)

    file_name="model/block/"+item_id+".json"
    with open(file_name,'w') as f:
        json.dump(text,f,indent=4)

def bi_model(item_id):
    result=["{",'   "parent":"cbs:block/'+item_id+'"','}']

    txt=""
    for x in result:
        txt=txt+x+"\n"

    text=json.loads(txt)

    file_name="model/item/"+item_id+".json"
    with open(file_name,'w') as f:
        json.dump(text,f,indent=4)

def name(item_type,item_id,names):
    list=['{']
    for i in range(0,len(names)):
        txt='   "'+item_type[i].lower()+'.cbs.'+item_id[i]+'":'+'"'+names[i]+'",'
        list.append(txt)
    list[-1]=list[-1][:-1]
    list.append('}')

    txt=""
    for x in list:
        txt=txt+x+"\n"

    text=json.loads(txt)

    file_name="lang/ja_jp.json"
    with open(file_name,'w') as f:
        json.dump(text,f,indent=4,ensure_ascii = False)



y=1
while True:
    y+=1
    c1=ws.cell(y,3)
    w=c1.value
    if(w==None):break
    item_model(w)
