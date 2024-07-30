<template>
    <div>
        <AdminNavbar />
        <div class="container contact-content">
            <h1>Contact Us</h1>
            <p>If you have any questions or need further assistance, please feel free to reach out to us:</p>
            <ul>
                <li>Email: support@example.com</li>
                <li>Phone: (123) 456-7890</li>
                <li>Address: 123 Main Street, Pune, Maharashtra</li>
            </ul>
        </div>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin/AdminNavbar.vue';

export default {
    components: {
        AdminNavbar
    }
};
</script>

<style scoped>
.contact-content {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    margin-top: 20px;
}

.contact-content h1 {
    color: #333;
    margin-bottom: 20px;
}

.contact-content p, .contact-content ul {
    color: #555;
    line-height: 1.6;
    margin-bottom: 15px;
}

.contact-content ul {
    list-style-type: none;
    padding-left: 0;
}

.contact-content li {
    margin-bottom: 10px;
}
</style>
