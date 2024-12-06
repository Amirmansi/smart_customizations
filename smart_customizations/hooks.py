from . import __version__ as app_version

app_name = "smart_customizations"
app_title = "Smart Customizations"
app_publisher = "Peter Maged"
app_description = "Smart Customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "eng.peter.maged@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
# Uncomment and ensure paths are valid for your ERPNext v15 setup
# app_include_css = "/assets/smart_customizations/css/smart_customizations.css"
# app_include_js = "/assets/smart_customizations/js/smart_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "smart_customizations/public/scss/website"

# Include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# DocType Class
# ---------------
# override standard doctype classes
# override_doctype_class = {
#    "ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
# doc_events = {
#    "*": {
#        "on_update": "method",
#        "on_cancel": "method",
#        "on_trash": "method"
#    }
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
#    "all": [
#        "smart_customizations.tasks.all"
#    ],
#    "daily": [
#        "smart_customizations.tasks.daily"
#    ],
#    "hourly": [
#        "smart_customizations.tasks.hourly"
#    ],
#    "weekly": [
#        "smart_customizations.tasks.weekly"
#    ],
#    "monthly": [
#        "smart_customizations.tasks.monthly"
#    ]
# }

# Testing
# -------
# before_tests = "smart_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
# override_whitelisted_methods = {
#    "frappe.desk.doctype.event.event.get_events": "smart_customizations.event.get_events"
# }
#
# override_doctype_dashboards = {
#    "Task": "smart_customizations.task.get_dashboard_data"
# }
