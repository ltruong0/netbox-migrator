class FilterModule:

    @staticmethod
    def filters():
        '''
        Filters will be called from here. Call from ansible playbook similar to a jinja filter

        Ex : " {{ variable | filter }} "

        First ARG is value that is before the | symbol, additional values can be passed

        "{{ ARG1 | filter(ARG2,ARG3) }}"
        '''

        return {
            'prep_netbox_objects' : FilterModule.prep_netbox_objects
        }


    @staticmethod
    def prep_netbox_objects(netbox_objects) -> dict:
        '''
        Simple filter for returned netbox objects from REST Api

        Args:
            netbox_objects : list of netbox api objects returned from GET call

        '''

        filtered_objects = {}
        for netbox_object in netbox_objects:

            if not filtered_objects.get(netbox_object['item']):
                filtered_objects[netbox_object['item']] = []
            
            filtered_objects[netbox_object['item']].extend(netbox_object['json']['results'])


        return filtered_objects