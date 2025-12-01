import uuid
import document_rev
import document_detail
def clint_registration(clint_list):
    clint_dict={}
    clint_dict["id"]=uuid.uuid4().hex[:10].upper()
    clint_dict["first_name"]=input("Please Enter Your First Name: ").lower()
    if clint_dict["first_name"].isalpha():
        clint_dict["last_name"]=input("Please enter your last Name: ").lower()
        if clint_dict["last_name"].isalpha():
            clint_dict["address"]=input("Please Enter Your Address: ")
            docs_list=document_detail.document_details()
            clint_dict["documents"]=docs_list
            document_rev.docs_review(clint_dict,clint_list)

    else:
        print("Please Register Again")  