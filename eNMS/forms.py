from eNMS.admin.forms import InstanceForm, UserForm
from eNMS.automation.forms import AddJobsForm, JobForm
from eNMS.inventory.forms import (
    ConnectionForm,
    DeviceAutomationForm,
    DeviceForm,
    LinkForm,
    PoolForm,
)
from eNMS.scheduling.forms import TaskForm

form_classes = {
    "add_jobs": AddJobsForm,
    "connection": ConnectionForm,
    "device": DeviceForm,
    "device_automation": DeviceAutomationForm,
    "instance": InstanceForm,
    "link": LinkForm,
    "pool": PoolForm,
    "user": UserForm,
    "service": JobForm,
    "task": TaskForm,
    "workflow": JobForm,
}

form_templates = {
    "add_jobs": "add_jobs_form",
    "connection": "connection_form",
    "device": "base_form",
    "device_automation": "device_automation_form",
    "instance": "base_form",
    "link": "base_form",
    "pool": "pool_form",
    "service": "service_form",
    "task": "base_form",
    "user": "base_form",
    "workflow": "workflow_form",
}

form_properties = {
    "add_jobs": ("add_jobs",),
    "advanced": ("clear_logs_date", "deletion_types", "import_export_types"),
    "configuration_management": ("restrict-pool",),
    "device_automation": ("jobs",),
    "device_management": ("restrict-pool",),
    "link": ("link-source", "link-destination"),
    "link_management": ("restrict-pool",),
    "service": ("devices", "pools"),
    "task": ("start_date", "end_date", "job"),
    "user": ("permissions", "pools"),
    "workflow": ("devices", "pools"),
}
