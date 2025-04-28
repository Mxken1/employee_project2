หน้าเเรก employee_list 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Employee Management</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: #262627;
            min-height: 100vh;
            font-family: 'Poppins', sans-serif;
            display: flex;
            flex-direction: column;
        }
        .navbar {
            background: linear-gradient(90deg, #1f1f1f, #3a3b3c);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
        }
        .navbar-brand {
            font-weight: bold;
            font-size: 1.5rem;
            letter-spacing: 1px;
        }
        .card {
            border: none;
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
        }
        table th {
            font-weight: 600;
        }
        .footer {
            margin-top: auto;
            background: linear-gradient(90deg, #1f1f1f, #3a3b3c);
            color: #bbb;
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'employee_list' %}">💼 Company</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'employee_list' %}">Home</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<!-- Content -->
<div class="container py-5 flex-grow-1">
    <div class="card p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h3 mb-0 text-light">🚀 Employee Management</h1>
            <a href="{% url 'add_employee' %}" class="btn btn-primary">+ Add Employee</a>
        </div>

        <form method="get" action="{% url 'employee_list' %}" class="input-group mb-4">
            <input type="text" name="search" placeholder="Search employees..." class="form-control" value="{{ request.GET.search }}">
            <button class="btn btn-outline-secondary" type="submit">Search</button>
        </form>

        <table class="table table-hover align-middle text-light">
            <thead class="table-light text-dark">
                <tr>
                    <th>Name</th>
                    <th>Position</th>
                    <th>Email</th>
                    <th class="text-center">Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for employee in employees %}
                <tr>
                    <td>{{ employee.name }}</td>
                    <td>{{ employee.position }}</td>
                    <td>{{ employee.email }}</td>
                    <td class="text-center">
                        <a href="{% url 'edit_employee' employee.id %}" class="btn btn-warning btn-sm">✏️ Edit</a>
                        <a href="{% url 'delete_employee' employee.id %}" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure you want to delete this employee?')">🗑️ Delete</a>
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="4" class="text-center">No employees found.</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>

<!-- Footer -->
<footer class="footer">
    © 2025 Company Inc. | Manage your team with ❤️
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
