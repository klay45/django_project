from django import forms
from django.forms import ModelForm
#from.models import Fish2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Employee
from.models import User
from.models import ID
from.models import AddID
from.models import DeptandDesignation
from django.utils.safestring import mark_safe



name_extension_choice=[
		('',''),
		('Jr.','Jr.'),
		('Sr.','Sr.'),
		('II','II'),
		
]

desig_choice=[
		('Select Designation','Select Designation'),
		('Accounting Analyst','Accounting Analyst'),
		('Accounting And Recording Audit Supervisor','Accounting And Recording Audit Supervisor'),
		('Accounting Processor','Accounting Processor'),
		('Accounts Payable Billing Processor','Accounts Payable Billing Processor'),
		('Accounts Payable Clerk Ii','Accounts Payable Clerk Ii'),
		('Accounts Payable Disbursement Clerk Ii','Accounts Payable Disbursement Clerk Ii'),
		('Accounts Payable Processor','Accounts Payable Processor'),
		('Accounts Payable Section Supervisor R13','Accounts Payable Section Supervisor R13'),
		('Accounts Payable Supervisor','Accounts Payable Supervisor'),
		('Accounts Receivable Processor','Accounts Receivable Processor'),
		('Accounts Receivables Section Supervisor','Accounts Receivables Section Supervisor'),
		('Accounts Receivables Supervisor','Accounts Receivables Supervisor'),
		('Admin Warehouseman','Admin Warehouseman'),
		('Administrative Associate','Administrative Associate'),
		('Administrative Liaison Officer','Administrative Liaison Officer'),
		('Administrative Processor','Administrative Processor'),
		('Administrative Support Processor','Administrative Support Processor'),
		('Administrative Warehouse Tender','Administrative Warehouse Tender'),
		('Aircon Technician','Aircon Technician'),
		('AP Billing Bookkeeper','AP Billing Bookkeeper'),
		('AP Billing Clerk','AP Billing Clerk'),
		('AP Disbursement Bookkeeper','AP Disbursement Bookkeeper'),
		('AP Disbursement Clerk','AP Disbursement Clerk'),
		('AP Disbursement Clerk (Aide)','AP Disbursement Clerk (Aide)'),
		('AP Disbursement Processor','AP Disbursement Processor'),
		('APprentice Auto-Electrician','APprentice Auto-Electrician'),
		('Asphalt Distributor Operator','Asphalt Distributor Operator'),
		('Asphalt Heating Operator','Asphalt Heating Operator'),
		('Asphalt Paver Operator','Asphalt Paver Operator'),
		('Asset Account Processor','Asset Account Processor'),
		('Assistant Plant Operator','Assistant Plant Operator'),
		('Associate Area Supervisor','Associate Area Supervisor'),
		('Auto Aircon Electrician','Auto Aircon Electrician'),
		('Auto Electrician','Auto Electrician'),
		('Auto Paintor','Auto Paintor'),
		('Backhoe Operator','Backhoe Operator'),
		('Barge Tender','Barge Tender'),
		('Battery Man','Battery Man'),
		('Bidding And Contracts Officer','Bidding And Contracts Officer'),
		('Battery Man','Battery Man'),
		('Battery Man','Battery Man'),
		('Bidding And Contracts Processor','Bidding And Contracts Processor'),
		('Billing Aide','Billing Aide'),
		('Billing Officer','Billing Officer'),
		('Billing Processor','Billing Processor'),
		('Billing Section Supervisor R10','Billing Section Supervisor R10'),
		('Boat Captain','Boat Captain'),
		('Body Builder','Body Builder'),
		('Bookkeeper','Bookkeeper'),
		('Bookkeeper Iii','Bookkeeper Iii'),
		('Boomtruck Driver','Boomtruck Driver'),
		('Branch Office Manager','Branch Office Manager'),
		('Budget Division Head','Budget Division Head'),
		('Budget Officer','Budget Officer'),
		('Budget Processor','Budget Processor'),
		('Bulldozer Operator','Bulldozer Operator'),
		('Cadd Operator','Cadd Operator'),
		('Calibrator Operator','Calibrator Operator'),
		('Canvasser','Canvasser'),
		('Canvassing Proccesor','Canvassing Proccesor'),
		('Canvassing Processor R13','Canvassing Processor R13'),
		('Checker','Checker'),
		('Chemical Laboratory Supervisor','Chemical Laboratory Supervisor'),
		('Chemist','Chemist'),
		('Canvassing Processor','Canvassing Processor'),
		('Checker','Checker'),
		('Chemical Laboratory Supervisor','Chemical Laboratory Supervisor'),
		('Chemist','Chemist'),
		('Chief Mate','Chief Mate'),
		('Civil 3d Operator','Civil 3d Operator'),
		('Clerical Processor','Clerical Processor'),
		('Cold Milling Machine Operator','Cold Milling Machine Operator'),
		('Collection Processor','Collection Processor'),
		('Collection Section Supervisor','Collection Section Supervisor'),
		('Company Nurse','Company Nurse'),
		('Compensation And Benefits Processor','Compensation And Benefits Processor'),
		('Compliance Bookkeeper','Compliance Bookkeeper'),
		('Compliance Clerk Ii','Compliance Clerk Ii'),
		('Compliance Section Supervisor','Compliance Section Supervisor'),
		('Concrete Paver Operator','Concrete Paver Operator'),
		('Concrete Pumpcrete Operator','Concrete Pumpcrete Operator'),
		('Concrete Pumptruck Operator','Concrete Pumptruck Operator'),
		('Contract Handling Processor','Contract Handling Processor'),
		('Cost Engineer','Cost Engineer'),
		('Crane Operator','Crane Operator'),
		('Crimping Machine Operator','Crimping Machine Operator'),
		('Diesel Hammer Operator','Diesel Hammer Operator'),
		('Disbursement And Collection Processor','Disbursement And Collection Processor'),
		('Disbursement And Collection Supervisort','Disbursement And Collection Supervisor'),
		('Disbursement Clerk','Disbursement Clerk'),
		('Disbursement Clerk Ii','Disbursement Clerk Ii'),
		('Disbursement Processor','Disbursement Processor'),
		('Disbursing Supervisor R10','Disbursing Supervisor R10'),
		('Disbursing Supervisor R13','Disbursing Supervisor R13'),
		('Document Controllert','Document Controller'),
		('Document Custodian','Document Custodian'),
		('Drilling Operator','Drilling Operator'),
		('Dumptruck Driver','Dumptruck Driver'),
		('Electrical Section Supervisor','Electrical Section Supervisor'),
		('Electrician','Electrician'),
		('Electronic Technician','Electronic Technician'),
		('Employee Relations Processor','Employee Relations Processor'),
		('Equipment And Rental Billing Analystchemist','Equipment And Rental Billing Analyst'),
		('Equipment Coordinator','Equipment Coordinator'),
		('Equipment History Analyst','Equipment History Analyst'),
		('Equipment Management Analyst','Equipment Management Analyst'),
		('Equipment Management Area Supervisor','Equipment Management Area Supervisor'),
		('Equipment Monitoring Processor','Equipment Monitoring Processor'),
		('Equipment Service Analyst R13','Equipment Service Analyst R13'),
		('Equipment Service Processor','Equipment Service Processor'),
		('Executive Assistant','Executive Assistant'),
		('Field Auditor','Field Auditor'),
		('Field Engineer','Field Engineer'),
		('Financial Reporting Bookkeeper','Financial Reporting Bookkeeper'),
		('First Aider','First Aider'),
		('Foreman','Foreman'),
		('Forester','Forester'),
		('Forklift Operator','Forklift Operator'),
		('Fuel Tanker Driver','Fuel Tanker Driver'),
		('Gasman','Gasman'),
		('Generator Technician','Generator Technician'),
		('Geodetic Engineer','Geodetic Engineer'),
		('GPS/CCTV Maintenance','GPS/CCTV Maintenance'),
		('Gsd Processor','Gsd Processor'),
		('Heating Operator','Heating Operator'),
		('Helper','Helper'),
		('HR Assistant','HR Assistant'),
		('Human Resource Generalist','Human Resource Generalist'),
		('Hydraulic Hammer Operator','Hydraulic Hammer Operator'),
		('IMD Reception','IMD Reception'),
		('IMD-Junior Parts Specialist','IMD-Junior Parts Specialist'),
		('Industrial Electrician','Industrial Electrician'),
		('Instrument Man','Instrument Man'),
		('Internal Audit System Assistant','Internal Audit System Assistant'),
		('Internal Control Financial Reporting Division Head','Internal Control Financial Reporting Division Head'),
		('Internal Security','Internal Security'),
		('Inventory Control Specialist','Inventory Control Specialist'),
		('Inventory Management Control Specialist','Inventory Management Control Specialist'),
		('Inventory Management Parts Specialist','Inventory Management Parts Specialist'),
		('Inventory Management Processor','Inventory Management Processor'),
		('Inventory Management Receiving Analyst','Inventory Management Receiving Analyst'),
		('Inventory Management Requisition Analyst','Inventory Management Requisition Analyst'),
		('Inventory Management Stock Analyst','Inventory Management Stock Analyst'),
		('Inventory Management Withdrawal Analyst','Inventory Management Withdrawal Analyst'),
		('Inventory Management Withdrawal Encoder','Inventory Management Withdrawal Encoder'),
		('Inventory Variance Report Processor','Inventory Variance Report Processor'),
		('Inventory Withdrawal Processor','Inventory Withdrawal Processor'),
		('IT Staff','IT Staff'),
		('IT Technician','IT Technician'),
		('Junior Mechanic','Junior Mechanic'),
		('Junior Project Manager','Junior Project Manager'),
		('Laboratory Aide','Laboratory Aide'),
		('Laboratory Technician','Laboratory Technician'),
		('Leadman','Leadman'),
		('Liaison Officer','Liaison Officer'),
		('Lube Stockman','Lube Stockman'),
		('Lubeman','Lubeman'),
		('Machine Shop Section Supervisor','Machine Shop Section Supervisor'),
		('Machinist','Machinist'),
		('Machinist Helper','Machinist Helper'),
		('Marine Equipment In-Charge','Marine Equipment In-Charge'),
		('Marketing Aide','Marketing Aide'),
		('Materials Assistant','Materials Assistant'),
		('Materials Engineer','Materials Engineer'),
		('Materials Receiving Processor','Materials Receiving Processor'),
		('Mechanic','Mechanic'),
		('Mechanical Section Supervisor','Mechanical Section Supervisor'),
		('Mini-Dumptruck Driver','Mini-Dumptruck Driver'),
		('Mini-Fuel Tanker Driver','Mini-Fuel Tanker Driver'),
		('Mining Engineer','Mining Engineer'),
		('Monitoring Engineer','Monitoring Engineer'),
		('Motorpool Maintenance Personnel','Motorpool Maintenance Personnel'),
		('Motorpool Supervisor (Iligan)','Motorpool Supervisor (Iligan)'),
		('Motorpool Technician','Motorpool Technician'),
		('Office Aide','Office Aide'),
		('Office Assistant','Office Assistant'),
		('Office Cashier','Office Cashier'),
		('Office Engineer','Office Engineer'),
		('Office Utility','Office Utility'),
		('OIC, Accounts Payable Section R10','OIC, Accounts Payable Section R10'),
		('OIC, Billing Section R13','OIC, Billing Section R13'),
		('OIC, Canvassing Division R13','OIC, Canvassing Division R13'),
		('OIC, Canvassing Section R10','OIC, Canvassing Section R10'),
		('OIC, Compensation And Benefits Section','OIC, Compensation And Benefits Section'),
		('OIC, Compliance Section','OIC, Compliance Section'),
		('OIC, Contracts And Handling Section','OIC, Contracts And Handling Section'),
		('OIC, Employee Relations Section','OIC, Employee Relations Section'),
		('OIC, Facilities Maintenance Section','OIC, Facilities Maintenance Section'),
		('OIC, IAS QMS Section','OIC, IAS QMS Section'),
		('OIC, Inventory Management Section 13','OIC, Inventory Management Section 13'),
		('OIC, Inventory Management Section R10','OIC, Inventory Management Section R10'),
		('OIC, Logistics Section R13','OIC, Logistics Section R13'),
		('OIC, MIS Section','OIC, MIS Section'),
		('OIC, Special License Handling Section','OIC, Special License Handling Section'),
		('Painter','Painter'),
		('Paving Block Operator/In-Charge','Paving Block Operator/In-Charge'),
		('Payloader Operator','Payloader Operator'),
		('Permits And Licenses Processor','Permits And Licenses Processor'),
		('Permits And Licenses Section Supervisor','Permits And Licenses Section Supervisor'),
		('Permits And Licensing Officer','Permits And Licensing Officer'),
		('Physical Labortory Supervisor','Physical Labortory Supervisor'),
		('Plant Account Analyst','Plant Account Analyst'),
		('Plant Aide','Plant Aide'),
		('Plant Electrician','Plant Electrician'),
		('Plant Maintenance','Plant Maintenance'),
		('Plant Operator','Plant Operator'),
		('Plant Processor','Plant Processor'),
		('Plant Supervisor','Plant Supervisor'),
		('Plant Technician','Plant Technician'),
		('Plants Processor','Plants Processor'),
		('PO Processor','PO Processor'),
		('Power Tool Technician','Power Tool Technician'),
		('Preventive Maintenance Compliance Officer','Preventive Maintenance Compliance Officer'),
		('Prime Mover Driver','Prime Mover Driver'),
		('Procurement Analyst R10','Procurement Analyst R10'),
		('Procurement Analyst R13','Procurement Analyst R13'),
		('Procurement Processor','Procurement Processor'),
		('Procurement Processor R13','Procurement Processor R13'),
		('Project Accounting Processor','Project Accounting Processor'),
		('Project Accounting Supervisor','Project Accounting Supervisor'),
		('Project Cashier','Project Cashier'),
		('Project Engineer','Project Engineer'),
		('Project Monitoring Section Supervisor','Project Monitoring Section Supervisor'),
		('Project Nurse','Project Nurse'),
		('Project Processor','Project Processor'),
		('Project Safety Aide','Project Safety Aide'),
		('Properties And Supply Processor','Properties And Supply Processor'),
		('Property And Supplies Division Head','Property And Supplies Division Head'),
		('Property Assistant','Property Assistant'),
		('Property Custodian','Property Custodian'),
		('Property In-Charge','Property In-Charge'),
		('Pumpboat Operator','Pumpboat Operator'),
		('Purchaser','Purchaser'),
		('Purchasing Processor','Purchasing Processor'),
		('QMS Assistant','QMS Assistant'),
		('Quality Control Engineer','Quality Control Engineer'),
		('Quantity Engineer','Quantity Engineer'),
		('Quarter Master','Quarter Master'),
		('Radiator Maintenance','Radiator Maintenance'),
		('Receiving Analyst','Receiving Analyst'),
		('Reconciliation Processor','Reconciliation Processor'),
		('Records Custodian','Records Custodian'),
		('Records In-Charge','Records In-Charge'),
		('Records Processor','Records Processor'),
		('Recruitment And Hiring Processor','Recruitment And Hiring Processor'),
		('Recruitment And Hiring Section Supervisor','Recruitment And Hiring Section Supervisor'),
		('Refinery Machine Operator','Refinery Machine Operator'),
		('Rigger','Rigger'),
		('Road Grader Operator','Road Grader Operator'),
		('Road Roller Operator','Road Roller Operator'),
		('Safety And Health Division Head','Safety And Health Division Head'),
		('Safety And Health Processor','Safety And Health Processor'),
		('Safety Officer','Safety Officer'),
		('Security Processor','Security Processor'),
		('Security Section Supervisor','Security Section Supervisor'),
		('Self Loader Driver','Self Loader Driver'),
		('Senior Electrician','Senior Electrician'),
		('Service Advisor','Service Advisor'),
		('Service Advisor Processor','Service Advisor Processor'),
		('Service Driver','Service Driver'),
		('Shuttle Bus Driver','Shuttle Bus Driver'),
		('Social Development Officer','Social Development Officer'),
		('Special License Compliance Processor','Special License Compliance Processor'),
		('Stake Truck Driver','Stake Truck Driver'),
		('Stock Analyst','Stock Analyst'),
		('Supply Officer','Supply Officer'),
		('Supply Processor','Supply Processor'),
		('Survey Aide','Survey Aide'),
		('Surveyor','Surveyor'),
		('Tarpaulin Production Assistant','Tarpaulin Production Assistant'),
		('Technical Assistant','Technical Assistant'),
		('Technical Engineer','Technical Engineer'),
		('Technical Officer','Technical Officer'),
		('Technical Services Processor','Technical Services Processor'),
		('Tender','Tender'),
		('Tenement Officer','Tenement Officer'),
		('Tireman','Tireman'),
		('Toolkeeper','Toolkeeper'),
		('Training And Development Section Supervisor','Training And Development Section Supervisorr'),
		('Training Associate','Training Associate'),
		('Transit Mixer Driver','Transit Mixer Driver'),
		('Treasury Aide','Treasury Aider'),
		('Treasury Processor','Treasury Processor'),
		('Truck Master','Truck Master'),
		('Truckscale Operator','Truckscale Operator'),
		('Turn-Over Processor','Turn-Over Processor'),
		('Vibro Hammer Operator','Vibro Hammer Operator'),
		('Warehouse Tender','Warehouse Tender'),
		('Warehouseman','Warehouseman'),
		('Water Truck Driver','Water Truck Driver'),
		('Welder','Welder'),
		('Welding Section Supervisor','Welding Section Supervisor'),
		('Welding Section Supervisor Withdrawal Analyst','Welding Section Supervisor Withdrawal Analyst'),







		

	]







class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

		
class ProfileUpdateForm(ModelForm):
	class Meta:

		model = Employee
		fields = ('midle_initial','name_extension','disignation','id_code','birth_date','address','contact_person','contact_person_no','contact_person_address','sss_no','tin','philhealth_no','blood_type','employee_no','id_pic','signature')
# Create your models here.


		labels = {

			'midle_initial': 'Middle Initial',
			'name_extension': 'Name Extension',
			'disignation': 'Designation',
			'id_code': 'ID Code',
			'birth_date': 'Birth Date',
			'address': 'Address',
			'contact_person': 'Contact Person',
			'contact_person_no': 'Contact Person No.',
			'contact_person_address': 'Contact Person Address',
			'sss_no':'SSS NO.',
			'tin':'TIN',
			'philhealth_no': 'PhilHealth No.',
			'blood_type': 'Blood Type',
			'employee_no': 'Employee Contact No.',
			'id_pic': 'Browse ID Pic',
			'signature': 'Browse Digital Signature',


		

		}
		widgets = {
			'midle_initial': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Middle Initial'}),
			#'name_extension': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Name Extension | Leave Blank if None'}),
			'name_extension': forms.Select(choices=name_extension_choice,attrs={'class':'form-control '}),
			'id_code': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter ID Code | Leave Blank if None'}),
			'birth_date': forms.TextInput(attrs={'class':'form-control ','placeholder':'Month/Day/Year'}),
			'disignation': forms.Select(choices=desig_choice,attrs={'class':'form-control '}),
			'address': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Address'}),
			'contact_person': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Contact Person Incase of Emergency'}),
			'contact_person_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Contact Person No.'}),
			'contact_person_address': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Contact Person Address'}),
			'sss_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter SSS No.'}),
			'tin': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter TIN'}),
			'philhealth_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter PhilHealth No.'}),
			'blood_type': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Blood Type'}),
			'employee_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Employee Contact Number'}),
			
		}


class AddIDForm(ModelForm):
	class Meta:

		model = AddID
		fields = ('first_name','midle_initial','last_name','name_extension','disignation','id_code','birth_date','address','contact_person','contact_person_no','contact_person_address','sss_no','tin','blood_type','employee_no','id_pic','signature')
# Create your models here.


		labels = {
			'first_name': 'First Name',
			'midle_initial': 'Middle Initial',
			'last_name': 'Last Name',
			'name_extension': 'Name Extension',
			'disignation': 'Designation',
			'id_code': 'ID Code',
			'birth_date': 'Birth Date',
			'address': 'Address',
			'contact_person': 'Contact Person',
			'contact_person_no': 'Contact Person No.',
			'contact_person_address': 'Contact Person Address',
			'sss_no':'SSS NO.',
			'tin':'TIN',
			'blood_type': 'Blood Type',
			'employee_no': 'Employee Contact No.',
			'id_pic': 'Browse ID Pic',
			'signature': 'Browse Digital Signature',


		

		}
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter First Name'}),
			'midle_initial': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Middle Initial'}),
			'last_name': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Last Name'}),
			#'name_extension': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Name Extension | Leave Blank if None'}),
			'name_extension': forms.Select(choices=name_extension_choice,attrs={'class':'form-control '}),
			'id_code': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter ID Code | Leave Blank if None'}),
			'birth_date': forms.TextInput(attrs={'class':'form-control ','placeholder':'Month/Day/Year'}),
			'disignation': forms.Select(choices=desig_choice,attrs={'class':'form-control '}),
			'address': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Address'}),
			'contact_person': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Contact Person Incase of Emergency'}),
			'contact_person_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Contact Person No.'}),
			'contact_person_address': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Contact Person Address'}),
			'sss_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter SSS No.'}),
			'tin': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter TIN'}),
			#'philhealth_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter PhilHealth No.'}),
			'blood_type': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Blood Type'}),
			'employee_no': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Employee Contact Number'}),
			
		}


		"""def __init__(self, *args, **kwargs):
			super(ProfileUpdateForm, self).__init__(*args, **kwargs)
			sorted_chOICes =sorted(Emloyee.STATE, key=lamda x: x[1])
			self.fields['disignation'].chOICes=sorted_chOICes"""

class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email',)

		labels = {


			'first_name': 'First Name',
			'last_name': 'Last Name',
			'email': 'Email',
			
			

		}
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter First hghfName'}),
			'last_name': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Last Name'}),
			'email': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Email'}),
		

			
		}

class UpdateIDForm(ModelForm):
	class Meta:
		model = ID
		fields =('status','user')
		labels ={
			'status':'Status',
			'user':'First Name'
		}
		widgets = {
			'status': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter First hghfName'}),
			'user.first_name': forms.TextInput(attrs={'class':'form-control ','placeholder':'Enter Last Name'}),

		}

class DeptandDesignationForm(ModelForm):
	


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['designation'].queryset = DeptandDesignation.objects.all()

	class Meta:
		model = DeptandDesignation
		fields =('designation',)
		labels ={
			'designation':'Designation',
			
		}
		widgets = {
			'designation': forms.Select(attrs={'class':'form-control '}),
			

		}



	
