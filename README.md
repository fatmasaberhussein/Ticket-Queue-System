# 🎫 Ticket Queue System__ نظام طابور التذاكر
---

## 📌 Description __ الوصف
 
A simple ticket queue management system built with Python.

نظام بسيط لإدارة طابور التذاكر تم بناؤه باستخدام Python.

The project uses the **Queue data structure** to manage customers based on the **FIFO (First In, First Out)** principle.

يستخدم المشروع **هيكل بيانات Queue (الطابور)** لإدارة العملاء وفقًا لمبدأ **FIFO (First In, First Out)**.

The first customer to enter the queue is the first customer to be served.

أول عميل يدخل الطابور هو أول عميل تتم خدمته.

---

## 🎯 Project Purpose __ ## 🎯 هدف المشروع


The purpose of this project is to apply the **Queue data structure** in a real-world scenario.

الهدف من هذا المشروع هو تطبيق **هيكل بيانات Queue** في سيناريو واقعي.

A ticket service system is a good example of a Queue because customers should normally be served in the same order they arrive.

يُعد نظام خدمة العملاء مثالًا مناسبًا للـ Queue لأن العملاء يجب عادةً أن تتم خدمتهم بنفس ترتيب وصولهم.

---

## ✨ Features ___ ## ✨ مميزات المشروع


* Add a customer to the queue
  إضافة عميل إلى الطابور

* Serve the first customer
  خدمة أول عميل في الطابور

* View the next customer
  معرفة العميل التالي

* Display all customers in the queue
  عرض جميع العملاء الموجودين في الطابور

* Display the number of customers in the queue
  عرض عدد العملاء الموجودين في الطابور

* Check whether the queue is empty
  التحقق مما إذا كان الطابور فارغًا

* Handle invalid menu choices
  التعامل مع الاختيارات غير الصحيحة في القائمة

* Exit the application safely
  الخروج من التطبيق بأمان

---

## 🧠 Data Structure ___ ## 🧠 هيكل البيانات


### Queue ___ ### الطابور

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

الـ **Queue** هيكل بيانات خطي يتبع مبدأ **FIFO (First In, First Out)**.

This means that the first element added to the queue is the first element removed.

وهذا يعني أن أول عنصر تتم إضافته إلى الطابور هو أول عنصر تتم إزالته منه.

Example:

مثال:

```text
Ahmed → Sara → Mohamed
  ↓
First customer served
```

أحمد → سارة → محمد
↓
أول عميل تتم خدمته

---

## 🔧 Queue Operations ___ ## 🔧 عمليات الـ Queue


### `enqueue()`

Adds a new customer to the end of the queue.

تضيف عميلًا جديدًا إلى نهاية الطابور.

```python
queue.enqueue("Ahmed")
```

---

### `dequeue()`

Removes and returns the first customer in the queue.

تزيل أول عميل من الطابور وتعيده.

```python
served_customer = queue.dequeue()
```

---

### `peek()`

Returns the first customer without removing them.

تعيد أول عميل بدون إزالته من الطابور.

```python
next_customer = queue.peek()
```

---

### `is_empty()`

Checks whether the queue contains any customers.

تتحقق مما إذا كان الطابور يحتوي على أي عملاء.

```python
queue.is_empty()
```

---

### `size()`

Returns the number of customers currently in the queue.

تعيد عدد العملاء الموجودين حاليًا في الطابور.

```python
queue.size()
```

---

## 🛠️ Technologies Used _ ## 🛠️ التقنيات والمفاهيم المستخدمة


* Python
  بايثون

* Object-Oriented Programming (OOP)
  البرمجة كائنية التوجه

* Data Structures
  هياكل البيانات

* Queue
  الطابور

* Lists
  القوائم

* Git & GitHub
  Git وGitHub

---

## 📁 Project Structure __ ## 📁 هيكل المشروع


```text
🎫 Ticket Queue System/
│
├── main.py
├── queue.py
└── README.md
```

### `main.py`

Contains the main application logic, menu, and user interaction.

يحتوي على منطق التطبيق الرئيسي، والقائمة، والتفاعل مع المستخدم.

### `queue.py`

Contains the `Queue` class and its operations.

يحتوي على `Queue Class` وعمليات الطابور.

### `README.md`

Contains the project documentation.

يحتوي على توثيق المشروع.

---

## ▶️ How to Run __ ## ▶️ كيفية تشغيل المشروع



Make sure Python is installed on your computer.

تأكد من تثبيت Python على جهاز الكمبيوتر.

Open the project folder in the terminal and run:

افتح مجلد المشروع في الـ Terminal وشغّل:

```bash
python main.py
```

The application will display a menu:

سيعرض التطبيق قائمة:

```text
===== Ticket Queue System =====
1. Add Customer
2. Serve Customer
3. View Next Customer
4. Show Queue
5. Show Queue Size
6. Exit
```

Enter the number of the operation you want to perform.

أدخل رقم العملية التي تريد تنفيذها.

---

## 💻 Example ____ ## 💻 مثال


A customer is added:

تمت إضافة عميل:

```text
Enter your choice: 1
Enter customer name: Ahmed
Customer added successfully.
```

Another customer is added:

تمت إضافة عميل آخر:

```text
Enter your choice: 1
Enter customer name: Sara
Customer added successfully.
```

When serving a customer:

عند خدمة أحد العملاء:

```text
Enter your choice: 2
Served: Ahmed
```

The first customer who entered the queue was served first, following the FIFO principle.

تمت خدمة أول عميل دخل إلى الطابور أولًا، وفقًا لمبدأ FIFO.

---

## 🧪 Input Validation ___ ## 🧪 التحقق من الإدخال


The program handles invalid menu choices.

يتعامل البرنامج مع الاختيارات غير الصحيحة في القائمة.

For example:

على سبيل المثال:

```text
Enter your choice: 7
Invalid choice. Please try again.
```

The program continues running instead of terminating.

يستمر البرنامج في العمل بدلًا من التوقف.

---

## 📚 What I Practiced __ ## 📚 ما الذي تدربت عليه؟


Through this project, I practiced:

من خلال هذا المشروع، تدربت على:

* Creating a custom data structure using a Python class
  إنشاء هيكل بيانات مخصص باستخدام Python Class

* Working with classes and objects
  التعامل مع الـ Classes والـ Objects

* Using `self`
  استخدام `self`

* Creating and calling methods
  إنشاء واستدعاء الـ Methods

* Using lists to store data
  استخدام القوائم لتخزين البيانات

* Using `append()` and `pop()`
  استخدام `append()` و`pop()`

* Working with indexes
  التعامل مع الـ Indexes

* Using `return`
  استخدام `return`

* Using `if`, `elif`, and `else`
  استخدام `if` و`elif` و`else`

* Using `while` loops
  استخدام حلقات `while`

* Handling user input with `input()`
  التعامل مع إدخال المستخدم باستخدام `input()`

* Importing a class from another Python file
  استيراد Class من ملف Python آخر

* Separating project responsibilities across files
  فصل مسؤوليات المشروع بين عدة ملفات

* Applying the FIFO principle
  تطبيق مبدأ FIFO

* Building an interactive command-line application
  بناء تطبيق تفاعلي يعمل من خلال سطر الأوامر

---

## 🚀 Future Improvements __ ## 🚀 التطويرات المستقبلية


Possible future improvements include:

تشمل التطويرات المستقبلية المحتملة:

* Adding ticket numbers
  إضافة أرقام للتذاكر

* Adding customer information
  إضافة بيانات خاصة بالعملاء

* Adding priority customers
  إضافة نظام للعملاء ذوي الأولوية

* Saving queue data to a file
  حفظ بيانات الطابور في ملف

* Adding a graphical user interface (GUI)
  إضافة واجهة رسومية للمستخدم

* Improving input validation
  تحسين التحقق من إدخالات المستخدم

* Adding automated tests
  إضافة اختبارات آلية

---

## 👩‍💻 Author ___ ## 👩‍💻 المطورة


**Fatma Saber Hussein**

**فاطمة صابر حسين**

This project was created as part of my Python and Data Structures learning journey.

تم إنشاء هذا المشروع كجزء من رحلة تعلم Python وهياكل البيانات.
