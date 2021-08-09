# Smart-Irrigation-System (Django Project)

## 1. Documentation:
### 1.1 Poblem Statement:
- Agriculture constitutes the largest sector of our economy, many Pakistani families relied on
agriculture as their main source of food and their main source of income as well. In the quarantine
of Covid-19 many farmers were unable to get into their farms causing unexpected loss. We are
mainly proposing a smart irrigation system to determine the exact amount of watering needs to a
plant and the solution relies on multiple low power sensors.
- Crops can be watered in many ways either through proper canal channels we can use
ground water or irrigation from hydraulic dam or rain water as well. By using many factors
like soil type, texture and state or climate, farmers plan for the crops that gives them the
best yield and profits.
- Rising water issues and events like Covid raised concerns in agriculture industry to tackle
these issues. A proposed solution is smart irrigation system which is composed of internet
of things (IoT) and machine learning also very cost effective to get the precise solution to
the farming and agriculture industry. A system whose purpose would be to overlook
conditions and situation of soil and also solve the irrigation problems and this way the over
wastage of water would be minimized.

### 1.2 Objective:
- To provide a practical sustainable monitoring system on self and remote-control
capabilities of automatic irrigation of water to the crops and plants. All data will be
collected real time with multi-sensing mechanism that will be analyzed with machine
learning.
- A sustainable design having low cost, long range, low power sensors working on the
Internet of Things (IoT) infrastructure to have the better understanding of the soil and
irrigation needs inside the farm.
- Reducing the water wastage happening during the irrigation process and also document the
findings of the information regarding soil and agricultural water requirements.

### 1.3 Features Of Project:
- Our solution will monitor the crops or plants in field and also administer the precise
amount of water needed only when necessary.
- Our solution uses smart IoT devices and sensors to measure the soil moisture in order to
determine that plant needs to watered or not.
- A WebApp to monitor the area of the land that consists the IoT devices and smart sensors
which measure the moisture after every fixed time period.
- Action will be taken on the basis of moisture threshold for any specific plant. If current
threshold is to be found lower then the water pump will be turned on until the moisture
level passes the threshold.

https://user-images.githubusercontent.com/46293412/128762330-f9ab567a-1337-4514-a759-2aedc5296965.jpg

### 1.4 Implementation Tools and Techniques:
#### 1.4.1 Our system is composed of the following components and modules:
- A database containing the known plants and the web app would tell the user about the state
of his fields. Machine learning models for sensor values and plant recognition and the IoT
devices which contains the soil moisture sensor, water pump and NodeMCU and finally a
server that will interface with all of the other components. Many other tools are also
required for the development are Django, Python and Machine Learning.

## 2. Project Installation Guide:
### 2.1 Project Requirements:
- Install Python in your system: https://www.python.org/downloads/
- Install Django Framework in your system via cmd: pip install django
- In this project we are using 3.2.6 (it is optional)

### 2.2 Project Commands (if you want to create your own project (OPTIONAL) ):
#### 2.2.1 Create Project:
- django-admin startproject Smart_Irrigation_System
#### 2.2.2 Create App:
- python manage.py startapp SIS_APP
#### 2.2.3 Run Server:
- python manage.py runserver
#### 2.2.4 Make Migrations:
- python manage.py makemigrations
#### 2.2.5 Make Migrate:
- python manage.py migrate
#### 2.2.6 Create Super User:
- python manage.py createsuperuser

### 2.3 Project Commands (if you run this project!)
#### 2.3.1 First Clone this project:
- git clone https://github.com/itxmujahidali/Smart-Irrigation-System.git
- Find manage.py file and open cmd at the same path where manage.py file exist!
#### 2.3.2 Run Server
- python manage.py runserver
