from flask_restful import Resource, Api
from TransGraphtion import db,app
from TransGraphtion.Models import Accounts,Transactions,UserInteractions
class FieldsData(Resource):
    def get(self):
        return { 
    "edges_fields": [ 
        { 
            "field_name": "id", 
            "type": "string" 
        }, 
        { 
            "field_name": "source", 
            "type": "string" 
        }, 
        { 
            "field_name": "target", 
            "type": "string" 
        }, 
        { 
            "field_name": "mainStat", 
            "type": "string" 
        }, 
        { 
            "field_name": "secondaryStat", 
            "type": "string" 
        } 
    ], 
    "nodes_fields": [ 
        { 
            "field_name": "id", 
            "type": "string" 
        }, 
        { 
            "field_name": "title", 
            "type": "string" 
        }, 
        { 
            "field_name": "mainStat", 
            "type": "string" 
        }, 
        { 
            "field_name": "secondaryStat", 
            "type": "string" 
        }, 
        { 
            "color": "red", 
            "field_name": "arc__failed", 
            "type": "number" 
        }, 
        { 
            "color": "green", 
            "field_name": "arc__passed", 
            "type": "number" 
        }, 
        { 
            "displayName": "Role", 
            "field_name": "detail__role", 
            "type": "string" 
        } 
    ] 
}
        
class AccountRest(Resource):
    def get(self):
        act=Accounts.query.get(1)
        if act!= None:
            edgecounter=1
            nodecounter=1
            returnvalue={"edges":[],"nodes":[{"arc__failed": 0.7, 
            "arc__passed": 0.3, 
            "id": nodecounter, 
            "subTitle": act.aadharid, 
            "mainStat": "Balance is "+act.transactions[-1].transactionbalance+"\n Click here to view full profile.", 
            "title": act.username +" - "+act.account_address }]}
            nodecounter+=1
            for i in act.transactions:
                if i.transactiontype!="Others" and (i.receipentaddress!="" or i.receipentaddress!="SELF"):
                    edge={"id": str(edgecounter),"mainStat": i.transactionid +" through "+i.transactiontype,
                          "secondaryStat": act.account_address +" - "+ i.receipentaddress,"source": "3", "target":  str(nodecounter)}
                    node={"arc__failed": 0.7, "arc__passed": 0.3, "id": str(nodecounter),
                        "mainStat": "Click here to view full profile.", "title": i.receipentaddress}
                    returnvalue["edges"].append(edge)
                    returnvalue["nodes"].append(node)
                    edgecounter+=1
                    nodecounter+=1
                    if nodecounter==50:
                        break
            return returnvalue

class HealthRest(Resource):
    def get(self):
        return "",200