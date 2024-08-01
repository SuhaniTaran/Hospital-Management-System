from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP, fill=X)

#==========================================DataFrame================================================================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft= LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)
        DataframeRight= LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)
#===================================================Buttons Frame===================================================================================


        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)


#===================================================Details Frame===================================================================================


        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
 

#=========================================================Dataframe left=======================================================================================

        lblNameTablet=Label(DataframeLeft,text="Name Of Tablet", font=("times new roman",12,"bold"),padx=2, pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,font=("times new roman",12,"bold"),width=33)
        comNametablet["values"]=("Nice", "corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.grid(row=0,column=1)

        lblref= Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No.:",padx=2)
        lblref.grid(row=1, column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1, column=1)

        lblDose= Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2, column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets= Label(DataframeLeft,font=("arial",12,"bold"),text="No. Of Tablets:",padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNoOftablets.grid(row=3, column=1)

        lbllot= Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2, pady=6)
        lbllot.grid(row=4, column=0,sticky=W)
        txtlot=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtlot.grid(row=4, column=1)

        lblissuedate= Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2, pady=6)
        lblissuedate.grid(row=5, column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate= Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2, pady=6)
        lblExpDate.grid(row=6, column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose= Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7, column=1)

        lblFurtherinfo= Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0, column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblSideEffect= Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8, column=1)

        lblBloodPressure= Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage= Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2, pady=6)
        lblSideEffect.grid(row=2, column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine= Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2, pady=6)
        lblMedicine.grid(row=3, column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId= Label(DataframeLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2, pady=6)
        lblPatientId.grid(row=4, column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber= Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientame= Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2, pady=6)
        lblPatientame.grid(row=6, column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientname.grid(row=6, column=3)

        lblDateOfBirth= Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress= Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientAddress.grid(row=8, column=3)

#==============================================Data FrameRight================================================
        self.txtPerscription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16, padx=2, pady=6)
        self.txtPerscription.grid(row=0,column=0)

#======================================================Buttons=======================================================================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"),width=23,padx=2,pady=4)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"),width=23,padx=2,pady=4)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update Prescription", bg="green", fg="white", font=("arial", 12, "bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete Prescription", bg="green", fg="white", font=("arial", 12, "bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0, column=5)
        
#===============================================table===============================================================
#=========================================================Scroollbar=================================================================================
        
        
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        FrameDetails = Frame(self.root, bd=2, relief=RIDGE)
        FrameDetails.place(x=20, y=620, width=1470, height=400)

        self.hospital_table = ttk.Treeview(FrameDetails, columns=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text="Name Of")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)


        self.hospital_table.column("nameoftable", width=100)

        self.hospital_table.column("ref",width=100) 
        
        self.hospital_table.column("dose",width=100)      
        
        self.hospital_table.column("nooftablets", width=100)

        self.hospital_table.column("lot", width=100)

        self.hospital_table.column("issuedate", width=100)

        self.hospital_table.column("expdate", width=100)

        self.hospital_table.column("dailydose", width=100)

        self.hospital_table.column("storage", width=100)

        self.hospital_table.column("nhsnumber", width=100)

        self.hospital_table.column("pname", width=100)

        self.hospital_table.column("dob", width=100)

        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

        





root = Tk()
ob = Hospital(root)
root.mainloop()