# 🛡️ Insurance Management System

This is a web-based Insurance Management System developed using Python and Django. The system is designed to manage customer insurance policies, handle claims, and facilitate interactions between customers and administrators.

## 📌 Project Description

The system allows administrators to manage insurance categories, policies, customers, and claims. Customers can register, log in, apply for policies, submit claims, and ask questions regarding their policies.

The project is divided into two main Django apps:
- `insurance` (Admin functionalities)
- `customer` (Customer functionalities)

## 🚀 Features

### Admin
- Admin account can be created using createsuperuser command.
- After login, admin can view/update/delete customer
- Can view/add/update/delete policy category like Life, Health, Motor, Travel
- Can view/add/update/delete policy
- Can view total policy holder, approved policy holder, disapproved policy holder
- Can approve policy, applied by customer
- Can answer customer question

### Customer
- Create account (no approval required by admin)
- After login, can view all policy that are added by admin.
- If customer likes any policy, then they can apply for it.
- When customer will apply for any policy, it will go into pending status, admin can approve it.
- Customer can check status of his policy under history section
- Customer can ask question from admin. 


### 👤 Admin Panel
- Login to admin dashboard
- Manage policy categories  
  ![Admin Category](screenshots/admin_category.PNG)
- Manage customers  
  ![Admin Customer](screenshots/admin_customer.PNG)
- Add/update/delete insurance policies  
  ![Admin Policy](screenshots/admin_policy.PNG)
- View and answer customer questions  
  ![Admin Question](screenshots/admin_question.PNG)
- Approve or disapprove policy applications  
  ![Approved Policy Holder](screenshots/approved_policy_holder.PNG)  
  ![Disapproved Policy](screenshots/disapproved_policy.PNG)
- View and manage submitted claims  
  ![Manage Claims](screenshots/manageclaims.PNG)
- Generate policy reports  
  ![Policy Report](screenshots/policy_report.PNG)

### 🧑‍💼 Customer Portal
- Sign up and log in  
  ![Signup](screenshots/signup.PNG)  
  ![Login](screenshots/login.PNG)
- Dashboard to view policy and account status  
  ![Customer Dashboard](screenshots/customerdashboard.PNG)
- Apply for insurance policies  
  ![Apply Policy](screenshots/applypolicy.PNG)
- View history of applied policies  
  ![Policy History](screenshots/policyhistory.PNG)
- Submit claims with reason, amount, and supporting documents  
  ![Claim Form](screenshots/claimform.PNG)
- Ask questions to the admin  
  ![Ask Question](screenshots/askquestion.PNG)
- View question history  
  ![Question History](screenshots/questionhistory.PNG)
- Track policy status: waiting or approved  
  ![Policy Holder Waiting](screenshots/policy_holder_waiting.PNG)
- View approved policy details  
  ![Policy Holder Record](screenshots/policy_holder_record.PNG)
- Contact page for support  
  ![Contact Us](screenshots/contactus.PNG)

### 🌐 Public Pages
- Homepage  
  ![Homepage](screenshots/homepage.PNG)
- Main landing page  
  ![Index](screenshots/index.PNG)


## ⚙️ Technologies Used

- Python
- Django Web Framework
- HTML/CSS/Bootstrap (for UI)
- SQLite (Default Django database)

## 🧭 How to Run

1. Clone this repository
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   py manage.py makemigrations
   py manage.py migrate
3. py manage.py runserver
