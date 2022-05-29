# Netbox Migrator
> Ansible Role to Migrate NetBox Environments

## Setup
---

### Python Setup
> The `pynetbox` module needs to be installed for this role
```
# Setup Virtual Env
python3 -m venv venv

# activate Virtual Env
source venv/bin/activate

# install requirements
pip3 install -r requirements.txt
```

### Ansible Collection Setup
> The `netbox.netbox` Collection is required for this role
```
ansible-galaxy install -r collections/requirements.yml
```

## Configuration
---
> Overview of configuration variables
```yaml
---
# defaults file for netbox-migrator
source_netbox_host: demo.netbox.dev
source_netbox_token: b457ea1acfc85aa711561f22bcb8f7f5e41ad2ca

destination_netbox_host: 192.168.1.34:8000
destination_netbox_token: 0123456789abcdef0123456789abcdef01234567

# define objects and resources to include in migration
netbox_objects:
  - endpoint: ipam
    resources:
      - ip-addresses
  - endpoint: tenancy
    resources:
      - tenants

```

- `source_netbox_host` : The netbox host to copy resources from.  
- `source_netbox_token` : API token for source netbox host
- `destination_netbox_host` : The netbox host to copy resources to.
- `destination_netbox_token` : API token for destination netbox host

- `netbox_objects` : list of endpoints to gather from
  - `endpoint`: netbox endpoint
    - `resources`: list of resources for specified endpoint

## Usage
---
Running the playbook
```
ansible-playbook playbook.yml
```

## References
---
- https://docs.ansible.com/ansible/latest/collections/netbox/netbox/index.html#plugins-in-netbox-netbox