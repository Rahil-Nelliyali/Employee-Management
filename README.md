# Employee Management System

The Employee Management System is a Django-based web application that allows users to manage employees within a company. It provides functionality to add, delete, edit, and filter employees through a user-friendly interface. The system also includes a login functionality to ensure secure access to the website.

## Features

- **Employee Management:** Add, delete, and edit employee details such as name, position, department, and contact information.
- **Employee Filtering:** Filter employees based on various criteria such as department, position, or name to easily find specific employees.
- **User Authentication:** Users can create an account and log in to access the system. This ensures that only authorized users can manage employee information.
- **User Roles:** Differentiate between administrators and regular users. Administrators have full access to manage employees, while regular users may have restricted permissions.
- **User Profile:** Users can view and update their profile information, such as name, email, and password, to maintain accurate and secure account details.
- **Responsive Design:** The application is designed to provide an optimal viewing experience across a range of devices, including desktops, tablets, and mobile phones.

## Installation

To run the Employee Management System locally, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/Rahil-Nelliyali/Employee-Management.git
```

2. Change into the project directory:

```shell
cd employee-management-system
```

3. Create a virtual environment (optional but recommended) and activate it:

```shell
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```shell
pip install -r requirements.txt
```

5. Set up the database:

```shell
python manage.py migrate
```

6. Create a superuser account (administrator) to access the admin interface:

```shell
python manage.py createsuperuser
```

7. Run the development server:

```shell
python manage.py runserver
```

8. Open your web browser and visit `http://localhost:8000` to access the Employee Management System.

## Configuration

The Employee Management System can be configured by modifying the `settings.py` file located in the `employee_management_system` directory. Here are a few key configuration options:

- **Database:** By default, the application uses an SQLite database. You can configure other databases such as PostgreSQL or MySQL by modifying the `DATABASES` settings in `settings.py`.
- **Static Files:** Static files (CSS, JavaScript, etc.) are stored in the `static` directory. If you need to change the location or configure a CDN, update the `STATIC_URL` and `STATIC_ROOT` settings accordingly.
- **Media Files:** Employee profile pictures or other uploaded files are stored in the `media` directory. Modify the `MEDIA_URL` and `MEDIA_ROOT` settings if you want to change the storage location or configure a CDN.

## Usage

1. Visit `http://localhost:8000` in your web browser.
2. If you have an existing account, log in. Otherwise, click on the "Sign Up" link to create a new account.
3. Once logged in, you can perform various employee management operations, such as adding, deleting, editing, and filtering employees.
4. To access the admin interface and manage user roles and permissions, visit `http://localhost:8000/admin` and log in using the superuser account created during installation.

## Contributing

Contributions to the Employee Management System are welcome! If you find a bug, have a feature request, or want to contribute enhancements, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
```

shell
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```shell
git commit -m "Your detailed explanation of your changes."
```
4. Push your changes to the branch:
```shell
git push origin feature/your-feature-name
```
5. Open a pull request on the main repository's `main` branch and provide a detailed description of your changes.


## Acknowledgments

The Employee Management System is built upon the Django web framework and utilizes several open-source libraries and tools. The following resources were instrumental in developing this project:

- Django: https://www.djangoproject.com/
- Bootstrap: https://getbootstrap.com/
- Font Awesome: https://fontawesome.com/
- jQuery: https://jquery.com/



## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the project maintainer:

- Name: Rahil Nelliyali
- Email: rahilnelliyali0@gmail.com
- GitHub: [Rahil Nelliyali](https://github.com/Rahil-Nelliyali)

Thank you for using the Employee Management System! We hope it helps streamline your employee management tasks.
