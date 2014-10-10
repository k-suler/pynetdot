import pynetdot.netdot as n
import pynetdot.fields as f
import pynetdot.models

class BaseArpCache(n.Netdot):
    resource = 'ArpCache/'
    id_field = 'id'
    _fields = [
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.DateTimeField('tstamp', display_name='Timestamp'),
    ]
    _views = {'all': ['tstamp', 'device'], 'brief': ['tstamp', 'device']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['tstamp', 'device']])
        return l.strip()

    def entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(arpcache=self.id)


class BaseArpCacheEntry(n.Netdot):
    resource = 'ArpCacheEntry/'
    id_field = 'id'
    _fields = [
        f.LinkField('arpcache', display_name='ARP Cache', link_to='ArpCache'),
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.LinkField('ipaddr', display_name='IP', link_to='Ipblock'),
        f.LinkField('physaddr', display_name='Physical Address', link_to='PhysAddr'),
    ]
    _views = {'all': ['interface', 'ipaddr', 'physaddr', 'arpcache'], 'brief': ['ipaddr', 'physaddr', 'interface']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['ipaddr', 'physaddr', 'interface']])
        return l.strip()


class BaseAsset(n.Netdot):
    resource = 'Asset/'
    id_field = 'id'
    _fields = [
        f.StringField('custom_serial', display_name='Custom S/N'),
        f.DateField('date_purchased', display_name='Date Purchased'),
        f.StringField('description', display_name='Description'),
        f.StringField('info', display_name='Comments'),
        f.StringField('inventory_number', display_name='Inventory'),
        f.LinkField('maint_contract', display_name='Maint Contract', link_to='MaintContract'),
        f.DateField('maint_from', display_name='Maint Start'),
        f.DateField('maint_until', display_name='Maint End'),
        f.LinkField('physaddr', display_name='Base MAC', link_to='PhysAddr'),
        f.StringField('po_number', display_name='PO Number'),
        f.LinkField('product_id', display_name='Product', link_to='Product'),
        f.StringField('reserved_for', display_name='Reserved For'),
        f.StringField('serial_number', display_name='S/N'),
    ]
    _views = {'all': ['serial_number', 'custom_serial', 'inventory_number', 'physaddr', 'product_id', 'description', 'po_number', 'reserved_for', 'date_purchased', 'maint_contract', 'maint_from', 'maint_until', 'info'], 'brief': ['serial_number', 'physaddr', 'product_id', 'inventory_number', 'maint_from', 'maint_until', 'reserved_for']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['product_id', 'serial_number', 'physaddr']])
        return l.strip()

    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(asset_id=self.id)

    def device_modules(self):
        cls = getattr(pynetdot.models, 'DeviceModule')
        return cls.search(asset_id=self.id)


class BaseAvailability(n.Netdot):
    resource = 'Availability/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Time Period'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def page_notifications(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(notify_email=self.id)

    def page_notifications(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(notify_pager=self.id)

    def page_notifications(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(notify_voice=self.id)

    def entities(self):
        cls = getattr(pynetdot.models, 'Entity')
        return cls.search(availability=self.id)

    def sites(self):
        cls = getattr(pynetdot.models, 'Site')
        return cls.search(availability=self.id)


class BaseBackboneCable(n.Netdot):
    resource = 'BackboneCable/'
    id_field = 'id'
    _fields = [
        f.LinkField('end_closet', display_name='Destination Closet', link_to='Closet'),
        f.StringField('info', display_name='Comments'),
        f.DateField('installdate', display_name='Installed on'),
        f.StringField('length', display_name='Length'),
        f.StringField('name', display_name='Cable ID'),
        f.LinkField('owner', display_name='Owned by', link_to='Entity'),
        f.LinkField('start_closet', display_name='Origin Closet', link_to='Closet'),
        f.LinkField('type', display_name='Cable Type', link_to='CableType'),
    ]
    _views = {'all': ['name', 'type', 'owner', 'installdate', 'start_closet', 'end_closet', 'length', 'info'], 'brief': ['name', 'start_closet', 'end_closet']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(cable=self.id)


class BaseBGPPeering(n.Netdot):
    resource = 'BGPPeering/'
    id_field = 'id'
    _fields = [
        f.StringField('authkey', display_name='Auth key'),
        f.StringField('bgppeeraddr', display_name='Peer Adress'),
        f.StringField('bgppeerid', display_name='Peer ID'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.StringField('info', display_name='Comments'),
        f.IntegerField('max_v4_prefixes', display_name='Max IPv4 Prefixes'),
        f.IntegerField('max_v6_prefixes', display_name='Max IPv6 Prefixes'),
        f.BoolField('monitored', display_name='Monitored?'),
        f.LinkField('monitorstatus', display_name='Monitored Status', link_to='MonitorStatus'),
    ]
    _views = {'all': ['device', 'entity', 'bgppeerid', 'bgppeeraddr', 'max_v4_prefixes', 'max_v6_prefixes', 'monitored', 'monitorstatus', 'authkey', 'info'], 'brief': ['device', 'entity', 'bgppeeraddr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['device', 'entity']])
        return l.strip()


class BaseCableStrand(n.Netdot):
    resource = 'CableStrand/'
    id_field = 'id'
    _fields = [
        f.LinkField('cable', display_name='Cable ID', link_to='BackboneCable'),
        f.LinkField('circuit_id', display_name='Circuit', link_to='Circuit'),
        f.StringField('description', display_name='Description'),
        f.LinkField('fiber_type', display_name='', link_to='FiberType'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Strand ID'),
        f.IntegerField('number', display_name='Number'),
        f.LinkField('status', display_name='Status', link_to='StrandStatus'),
    ]
    _views = {'all': ['name', 'number', 'cable', 'status', 'fiber_type', 'circuit_id', 'description', 'info'], 'brief': ['name', 'cable', 'status']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def splices(self):
        cls = getattr(pynetdot.models, 'Splice')
        return cls.search(strand1=self.id)

    def splices2(self):
        cls = getattr(pynetdot.models, 'Splice')
        return cls.search(strand2=self.id)


class BaseCableType(n.Netdot):
    resource = 'CableType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def backbonecables(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(type=self.id)

    def horizontalcables(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(type=self.id)


class BaseCircuit(n.Netdot):
    resource = 'Circuit/'
    id_field = 'id'
    _fields = [
        f.StringField('cid', display_name='Circuit ID'),
        f.DateField('datetested', display_name='Date Tested'),
        f.StringField('info', display_name='Comments'),
        f.DateField('installdate', display_name='Installed on'),
        f.LinkField('linkid', display_name='Site Link', link_to='SiteLink'),
        f.StringField('loss', display_name='Loss'),
        f.StringField('speed', display_name='Speed'),
        f.LinkField('status', display_name='Status', link_to='CircuitStatus'),
        f.LinkField('type', display_name='Type', link_to='CircuitType'),
        f.LinkField('vendor', display_name='Provider', link_to='Entity'),
    ]
    _views = {'all': ['cid', 'linkid', 'status', 'type', 'speed', 'installdate', 'datetested', 'loss', 'vendor', 'info'], 'brief': ['cid', 'linkid', 'type', 'vendor', 'status']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['cid']])
        return l.strip()

    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(circuit_id=self.id)

    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(circuit=self.id)


class BaseCircuitStatus(n.Netdot):
    resource = 'CircuitStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Status'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(status=self.id)


class BaseCircuitType(n.Netdot):
    resource = 'CircuitType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Type'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(type=self.id)


class BaseCloset(n.Netdot):
    resource = 'Closet/'
    id_field = 'id'
    _fields = [
        f.StringField('access_key_type', display_name='Access Key Type'),
        f.BoolField('asbestos_tiles', display_name='Asbestos Tiles'),
        f.StringField('catv_taps', display_name='CableTV Taps'),
        f.BoolField('converted_patch_panels', display_name='Converted Patch Panels'),
        f.StringField('dimensions', display_name='Dimensions (")'),
        f.BoolField('ground_buss', display_name='Ground Buss'),
        f.StringField('hvac_type', display_name='HVAC Type'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.StringField('ot_blocks', display_name='110 Blocks'),
        f.StringField('outlets', display_name='Outlets'),
        f.StringField('pair_count', display_name='Pair Count'),
        f.StringField('patch_panels', display_name='Patch Panels'),
        f.StringField('rack_type', display_name='Rack Type'),
        f.StringField('racks', display_name='Racks'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.StringField('ru_avail', display_name='Rack Units Available'),
        f.StringField('shared_with', display_name='Shared With'),
        f.StringField('ss_blocks', display_name='66 Blocks'),
        f.StringField('work_needed', display_name='Work Needed'),
    ]
    _views = {'all': ['name', 'room', 'dimensions', 'racks', 'outlets', 'ru_avail', 'patch_panels', 'ot_blocks', 'ss_blocks', 'catv_taps', 'access_key_type', 'work_needed', 'shared_with', 'hvac_type', 'ground_buss', 'asbestos_tiles', 'rack_type', 'pair_count', 'converted_patch_panels', 'info'], 'brief': ['name', 'room']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'room']])
        return l.strip()

    def backbones_end(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(end_closet=self.id)

    def backbones_start(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(start_closet=self.id)

    def horizontalcables(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(closet=self.id)


class BaseContact(n.Netdot):
    resource = 'Contact/'
    id_field = 'id'
    _fields = [
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.LinkField('contacttype', display_name='Type of Contact', link_to='ContactType'),
        f.IntegerField('escalation_level', display_name='Escalation Level'),
        f.StringField('info', display_name='Comments'),
        f.LinkField('notify_email', display_name='Email Notifications', link_to='Availability'),
        f.LinkField('notify_pager', display_name='Pager Notifications', link_to='Availability'),
        f.LinkField('notify_voice', display_name='Voice Notifications', link_to='Availability'),
        f.LinkField('person', display_name='Person', link_to='Person'),
    ]
    _views = {'all': ['person', 'contacttype', 'contactlist', 'notify_email', 'notify_pager', 'notify_voice', 'escalation_level', 'info'], 'brief': ['person', 'contacttype', 'contactlist']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['person', 'contacttype']])
        return l.strip()


class BaseContactList(n.Netdot):
    resource = 'ContactList/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name', 'info']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def contacts(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(contactlist=self.id)

    def devices(self):
        cls = getattr(pynetdot.models, 'DeviceContacts')
        return cls.search(contactlist=self.id)

    def entities(self):
        cls = getattr(pynetdot.models, 'Entity')
        return cls.search(contactlist=self.id)

    def access_rights(self):
        cls = getattr(pynetdot.models, 'GroupRight')
        return cls.search(contactlist=self.id)

    def outlets(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(contactlist=self.id)

    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(contactlist=self.id)

    def services(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(contactlist=self.id)

    def sites(self):
        cls = getattr(pynetdot.models, 'Site')
        return cls.search(contactlist=self.id)

    def zones(self):
        cls = getattr(pynetdot.models, 'Zone')
        return cls.search(contactlist=self.id)


class BaseContactType(n.Netdot):
    resource = 'ContactType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def contacts(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(contacttype=self.id)


class BaseDevice(n.Netdot):
    resource = 'Device/'
    id_field = 'id'
    _fields = [
        f.StringField('aliases', display_name='Aliases'),
        f.LinkField('asset_id', display_name='Asset', link_to='Asset'),
        f.BoolField('auto_dns', display_name='Auto DNS?'),
        f.StringField('bgpid', display_name='BGP ID'),
        f.IntegerField('bgplocalas', display_name='BGP Local AS'),
        f.BoolField('canautoupdate', display_name='Auto Update?'),
        f.BoolField('collect_arp', display_name='Collect ARP?'),
        f.BoolField('collect_fwt', display_name='Collect FWT?'),
        f.BoolField('collect_stp', display_name='Collect STP Info?'),
        f.StringField('community', display_name='SNMP Community'),
        f.BoolField('customer_managed', display_name='Managed by Customer?'),
        f.DateTimeField('date_installed', display_name='First Discovered'),
        f.DateField('down_from', display_name='Down From'),
        f.DateField('down_until', display_name='Down Until'),
        f.IntegerField('extension', display_name='Extension'),
        f.StringField('info', display_name='Comments'),
        f.BoolField('ipforwarding', display_name='IP Forward?'),
        f.DateTimeField('last_arp', display_name='Last ARP'),
        f.DateTimeField('last_fwt', display_name='Last FWT'),
        f.DateTimeField('last_updated', display_name='Last Updated'),
        f.StringField('layers', display_name='OSI Layers'),
        f.BoolField('monitor_config', display_name='Monitor Config?'),
        f.StringField('monitor_config_group', display_name='Config Group?'),
        f.BoolField('monitored', display_name='Monitored?'),
        f.IntegerField('monitoring_path_cost', display_name='Path Cost'),
        f.LinkField('monitorstatus', display_name='Monitored Status', link_to='MonitorStatus'),
        f.LinkField('name', display_name='Name', link_to='RR'),
        f.StringField('oobname', display_name='Out-of-Band Hostname'),
        f.StringField('oobnumber', display_name='Out-of-Band Tel Number'),
        f.StringField('os', display_name='OS'),
        f.LinkField('owner', display_name='Owner', link_to='Entity'),
        f.StringField('rack', display_name='Rack'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.LinkField('site', display_name='Site', link_to='Site'),
        f.StringField('snmp_authkey', display_name='AuthKey'),
        f.StringField('snmp_authprotocol', display_name='AuthProtocol'),
        f.BoolField('snmp_bulk', display_name='SNMP Bulk?'),
        f.IntegerField('snmp_conn_attempts', display_name='SNMP Failed Attempts'),
        f.BoolField('snmp_down', display_name='SNMP Down'),
        f.BoolField('snmp_managed', display_name='SNMP Managed?'),
        f.BoolField('snmp_polling', display_name='SNMP Polling?'),
        f.StringField('snmp_privkey', display_name='PrivKey'),
        f.StringField('snmp_privprotocol', display_name='PrivProtocol'),
        f.StringField('snmp_securitylevel', display_name='SecLevel'),
        f.StringField('snmp_securityname', display_name='SecName'),
        f.LinkField('snmp_target', display_name='SNMP Target Address', link_to='Ipblock'),
        f.IntegerField('snmp_version', display_name='SNMP Version'),
        f.BoolField('stp_enabled', display_name='STP Enabled?'),
        f.StringField('stp_mst_digest', display_name='MST Config Digest'),
        f.StringField('stp_mst_region', display_name='MST Region'),
        f.IntegerField('stp_mst_rev', display_name='MST Revision'),
        f.StringField('stp_type', display_name='STP Type'),
        f.StringField('sysdescription', display_name='System Description'),
        f.StringField('syslocation', display_name='System Location'),
        f.StringField('sysname', display_name='System Name'),
        f.LinkField('used_by', display_name='Used by', link_to='Entity'),
    ]
    _views = {'all': ['name', 'asset_id', 'aliases', 'snmp_target', 'sysname', 'sysdescription', 'syslocation', 'ipforwarding', 'layers', 'os', 'extension', 'bgplocalas', 'auto_dns', 'bgpid', 'oobname', 'oobnumber', 'owner', 'used_by', 'monitored', 'monitoring_path_cost', 'monitorstatus', 'customer_managed', 'community', 'canautoupdate', 'site', 'monitor_config', 'monitor_config_group', 'snmp_managed', 'snmp_polling', 'collect_arp', 'last_arp', 'collect_fwt', 'collect_stp', 'last_fwt', 'snmp_bulk', 'snmp_version', 'snmp_securityname', 'snmp_authkey', 'snmp_authprotocol', 'snmp_privkey', 'snmp_privprotocol', 'snmp_securitylevel', 'snmp_conn_attempts', 'snmp_down', 'stp_enabled', 'stp_type', 'stp_mst_region', 'stp_mst_rev', 'stp_mst_digest', 'room', 'rack', 'last_updated', 'date_installed', 'down_from', 'down_until', 'info'], 'brief': ['name', 'asset_id', 'site', 'snmp_target']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def arp_caches(self):
        cls = getattr(pynetdot.models, 'ArpCache')
        return cls.search(device=self.id)

    def bgppeers(self):
        cls = getattr(pynetdot.models, 'BGPPeering')
        return cls.search(device=self.id)

    def attributes(self):
        cls = getattr(pynetdot.models, 'DeviceAttr')
        return cls.search(device=self.id)

    def contacts(self):
        cls = getattr(pynetdot.models, 'DeviceContacts')
        return cls.search(device=self.id)

    def modules(self):
        cls = getattr(pynetdot.models, 'DeviceModule')
        return cls.search(device=self.id)

    def forwarding_tables(self):
        cls = getattr(pynetdot.models, 'FWTable')
        return cls.search(device=self.id)

    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(device=self.id)

    def stp_instances(self):
        cls = getattr(pynetdot.models, 'STPInstance')
        return cls.search(device=self.id)


class BaseDeviceAttr(n.Netdot):
    resource = 'DeviceAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.LinkField('name', display_name='Name', link_to='DeviceAttrName'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'device'], 'brief': ['name', 'value', 'device']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value', 'device']])
        return l.strip()


class BaseDeviceAttrName(n.Netdot):
    resource = 'DeviceAttrName/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def attributes(self):
        cls = getattr(pynetdot.models, 'DeviceAttr')
        return cls.search(name=self.id)


class BaseDeviceContacts(n.Netdot):
    resource = 'DeviceContacts/'
    id_field = 'id'
    _fields = [
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.LinkField('device', display_name='Device', link_to='Device'),
    ]
    _views = {'all': ['device', 'contactlist'], 'brief': ['device', 'contactlist']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['contactlist']])
        return l.strip()


class BaseDeviceModule(n.Netdot):
    resource = 'DeviceModule/'
    id_field = 'id'
    _fields = [
        f.LinkField('asset_id', display_name='Asset', link_to='Asset'),
        f.StringField('class', display_name='Class'),
        f.IntegerField('contained_in', display_name='Contained In'),
        f.DateTimeField('date_installed', display_name='First Discovered'),
        f.StringField('description', display_name='Description'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.BoolField('fru', display_name='FRU?'),
        f.StringField('fw_rev', display_name='Firmware Revision'),
        f.StringField('hw_rev', display_name='Hardware Revision'),
        f.DateTimeField('last_updated', display_name='Last Updated'),
        f.StringField('model', display_name='Model'),
        f.StringField('name', display_name='Name'),
        f.IntegerField('number', display_name='Number'),
        f.IntegerField('pos', display_name='Position'),
        f.StringField('sw_rev', display_name='Software Revision'),
        f.StringField('type', display_name='Type'),
    ]
    _views = {'all': ['device', 'contained_in', 'number', 'pos', 'name', 'type', 'class', 'description', 'model', 'hw_rev', 'fw_rev', 'sw_rev', 'fru', 'asset_id', 'date_installed', 'last_updated'], 'brief': ['number', 'name', 'class', 'model', 'description', 'asset_id']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'model', 'device']])
        return l.strip()


class BaseDhcpAttr(n.Netdot):
    resource = 'DhcpAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('name', display_name='Name', link_to='DhcpAttrName'),
        f.LinkField('scope', display_name='Scope', link_to='DhcpScope'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'scope'], 'brief': ['name', 'value', 'scope']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value']])
        return l.strip()


class BaseDhcpAttrName(n.Netdot):
    resource = 'DhcpAttrName/'
    id_field = 'id'
    _fields = [
        f.IntegerField('code', display_name='Code'),
        f.StringField('format', display_name='Format'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'code', 'format', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def attributes(self):
        cls = getattr(pynetdot.models, 'DhcpAttr')
        return cls.search(name=self.id)


class BaseDhcpScope(n.Netdot):
    resource = 'DhcpScope/'
    id_field = 'id'
    _fields = [
        f.BoolField('active', display_name='Active?'),
        f.LinkField('container', display_name='Container Scope', link_to='DhcpScope'),
        f.StringField('duid', display_name='DUID'),
        f.BoolField('enable_failover', display_name='Enable Failover?'),
        f.StringField('export_file', display_name='Export File'),
        f.StringField('failover_peer', display_name='Failover Peer'),
        f.LinkField('ipblock', display_name='IP block', link_to='Ipblock'),
        f.StringField('name', display_name='Name'),
        f.LinkField('physaddr', display_name='Ethernet', link_to='PhysAddr'),
        f.StringField('text', display_name='Include Text'),
        f.LinkField('type', display_name='Type', link_to='DhcpScopeType'),
        f.IntegerField('version', display_name='Version (4|6)'),
    ]
    _views = {'subnet': ['name', 'type', 'active', 'container', 'ipblock', 'enable_failover', 'failover_peer', 'text'], 'all': ['name', 'type', 'version', 'container', 'active', 'ipblock', 'physaddr', 'duid', 'text', 'enable_failover', 'failover_peer', 'export_file'], 'group': ['name', 'type', 'active', 'container', 'text'], 'global': ['name', 'type', 'version', 'active', 'enable_failover', 'failover_peer', 'export_file', 'text'], 'brief': ['name', 'type'], 'subclass': ['name', 'type', 'active', 'container', 'text'], 'host': ['name', 'type', 'active', 'container', 'ipblock', 'duid', 'physaddr', 'text'], 'shared-network': ['name', 'type', 'active', 'container', 'text'], 'class': ['name', 'type', 'active', 'container', 'text'], 'pool': ['name', 'type', 'active', 'container', 'text']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['type', 'name']])
        return l.strip()

    def attributes(self):
        cls = getattr(pynetdot.models, 'DhcpAttr')
        return cls.search(scope=self.id)

    def contained_scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(container=self.id)

    def templates(self):
        cls = getattr(pynetdot.models, 'DhcpScopeUse')
        return cls.search(scope=self.id)

    def derived_scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScopeUse')
        return cls.search(template=self.id)


class BaseDhcpScopeType(n.Netdot):
    resource = 'DhcpScopeType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(type=self.id)


class BaseDhcpScopeUse(n.Netdot):
    resource = 'DhcpScopeUse/'
    id_field = 'id'
    _fields = [
        f.LinkField('scope', display_name='Scope', link_to='DhcpScope'),
        f.LinkField('template', display_name='Template', link_to='DhcpScope'),
    ]
    _views = {'all': ['scope', 'template'], 'brief': ['scope', 'template']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['scope', 'template']])
        return l.strip()


class BaseEntity(n.Netdot):
    resource = 'Entity/'
    id_field = 'id'
    _fields = [
        f.StringField('acctnumber', display_name='Account Number'),
        f.StringField('aliases', display_name='Aliases'),
        f.StringField('asname', display_name='AS Name'),
        f.IntegerField('asnumber', display_name='AS Number'),
        f.LinkField('availability', display_name='Availability', link_to='Availability'),
        f.StringField('config_type', display_name='Config Type'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.StringField('info', display_name='Comments'),
        f.StringField('maint_contract', display_name='Maintenance Contract'),
        f.StringField('name', display_name='Name'),
        f.StringField('oid', display_name='Enterprise OID'),
        f.StringField('short_name', display_name='Short Name'),
    ]
    _views = {'peer': ['name', 'aliases', 'short_name', 'type', 'availability', 'contactlist', 'asname', 'asnumber', 'info'], 'all': ['name', 'aliases', 'short_name', 'availability', 'contactlist', 'acctnumber', 'maint_contract', 'asname', 'asnumber', 'oid', 'config_type', 'info'], 'provider': ['name', 'aliases', 'short_name', 'type', 'availability', 'contactlist', 'asname', 'asnumber', 'info'], 'brief': ['name', 'short_name'], 'manufacturer': ['name', 'aliases', 'short_name', 'type', 'contactlist', 'oid', 'config_type', 'info']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def bgppeers(self):
        cls = getattr(pynetdot.models, 'BGPPeering')
        return cls.search(entity=self.id)

    def cables(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(owner=self.id)

    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(vendor=self.id)

    def owned_devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(owner=self.id)

    def used_devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(used_by=self.id)

    def roles(self):
        cls = getattr(pynetdot.models, 'EntityRole')
        return cls.search(entity=self.id)

    def sites(self):
        cls = getattr(pynetdot.models, 'EntitySite')
        return cls.search(entity=self.id)

    def owned_blocks(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(owner=self.id)

    def used_blocks(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(used_by=self.id)

    def maintenance_contracts(self):
        cls = getattr(pynetdot.models, 'MaintContract')
        return cls.search(provider=self.id)

    def employees(self):
        cls = getattr(pynetdot.models, 'Person')
        return cls.search(entity=self.id)

    def products(self):
        cls = getattr(pynetdot.models, 'Product')
        return cls.search(manufacturer=self.id)

    def links(self):
        cls = getattr(pynetdot.models, 'SiteLink')
        return cls.search(entity=self.id)


class BaseEntityRole(n.Netdot):
    resource = 'EntityRole/'
    id_field = 'id'
    _fields = [
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.LinkField('type', display_name='Type', link_to='EntityType'),
    ]
    _views = {'all': ['entity', 'type'], 'brief': ['entity', 'type']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['entity', 'type']])
        return l.strip()


class BaseEntitySite(n.Netdot):
    resource = 'EntitySite/'
    id_field = 'id'
    _fields = [
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.LinkField('site', display_name='Site', link_to='Site'),
    ]
    _views = {'all': ['entity', 'site'], 'brief': ['entity', 'site']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['entity', 'site']])
        return l.strip()


class BaseEntityType(n.Netdot):
    resource = 'EntityType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def roles(self):
        cls = getattr(pynetdot.models, 'EntityRole')
        return cls.search(type=self.id)


class BaseFiberType(n.Netdot):
    resource = 'FiberType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(fiber_type=self.id)


class BaseFloor(n.Netdot):
    resource = 'Floor/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('level', display_name='Level'),
        f.LinkField('site', display_name='Site', link_to='Site'),
    ]
    _views = {'all': ['level', 'site', 'info'], 'brief': ['level', 'site']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['level', 'site']])
        return l.strip()

    def rooms(self):
        cls = getattr(pynetdot.models, 'Room')
        return cls.search(floor=self.id)


class BaseFWTable(n.Netdot):
    resource = 'FWTable/'
    id_field = 'id'
    _fields = [
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.DateTimeField('tstamp', display_name='Timestamp'),
    ]
    _views = {'all': ['tstamp', 'device'], 'brief': ['tstamp', 'device']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['tstamp', 'device']])
        return l.strip()

    def entries(self):
        cls = getattr(pynetdot.models, 'FWTableEntry')
        return cls.search(fwtable=self.id)


class BaseFWTableEntry(n.Netdot):
    resource = 'FWTableEntry/'
    id_field = 'id'
    _fields = [
        f.LinkField('fwtable', display_name='Table', link_to='FWTable'),
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.LinkField('physaddr', display_name='Physical Address', link_to='PhysAddr'),
    ]
    _views = {'all': ['interface', 'physaddr', 'fwtable'], 'brief': ['interface', 'physaddr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['interface', 'physaddr']])
        return l.strip()


class BaseGroupRight(n.Netdot):
    resource = 'GroupRight/'
    id_field = 'id'
    _fields = [
        f.LinkField('accessright', display_name='Access Right', link_to='AccessRight'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
    ]
    _views = {'all': ['contactlist', 'accessright'], 'brief': ['contactlist', 'accessright']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['contactlist', 'accessright']])
        return l.strip()


class BaseHorizontalCable(n.Netdot):
    resource = 'HorizontalCable/'
    id_field = 'id'
    _fields = [
        f.StringField('account', display_name='Account'),
        f.LinkField('closet', display_name='Closet', link_to='Closet'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.DateField('datetested', display_name='Date Tested'),
        f.StringField('faceplateid', display_name='Faceplate ID'),
        f.StringField('info', display_name='Comments'),
        f.DateField('installdate', display_name='Date Installed'),
        f.StringField('jackid', display_name='Jack ID'),
        f.StringField('length', display_name='Length'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.BoolField('testpassed', display_name='Passed Test?'),
        f.LinkField('type', display_name='Type', link_to='CableType'),
    ]
    _views = {'all': ['jackid', 'faceplateid', 'type', 'datetested', 'testpassed', 'installdate', 'length', 'closet', 'room', 'account', 'contactlist', 'info'], 'brief': ['jackid', 'closet', 'room']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['jackid']])
        return l.strip()

    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(jack=self.id)


class BaseHostAudit(n.Netdot):
    resource = 'HostAudit/'
    id_field = 'id'
    _fields = [
        f.BoolField('pending', display_name=''),
        f.StringField('scope', display_name='DHCP Scope'),
        f.DateTimeField('tstamp', display_name='Timestamp'),
        f.StringField('zone', display_name='Zone'),
    ]
    _views = {'all': ['tstamp', 'zone', 'scope', 'pending'], 'brief': ['tstamp', 'zone', 'scope', 'pending']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['zone']])
        return l.strip()


class BaseInterface(n.Netdot):
    resource = 'Interface/'
    id_field = 'id'
    _fields = [
        f.StringField('admin_duplex', display_name='Admin Duplex'),
        f.StringField('admin_status', display_name='Admin Status'),
        f.BoolField('auto_dns', display_name='Auto DNS?'),
        f.BoolField('bpdu_filter_enabled', display_name='BPDU Filter?'),
        f.BoolField('bpdu_guard_enabled', display_name='BPDU Guard?'),
        f.LinkField('circuit', display_name='Circuit', link_to='Circuit'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.StringField('description', display_name='Description'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.StringField('dlci', display_name='DLCI'),
        f.StringField('doc_status', display_name='Doc Status'),
        f.DateField('down_from', display_name='Down From'),
        f.DateField('down_until', display_name='Down Until'),
        f.StringField('dp_remote_id', display_name='DP Remote ID'),
        f.StringField('dp_remote_ip', display_name='DP Remote IP'),
        f.StringField('dp_remote_port', display_name='DP Remote Port'),
        f.StringField('dp_remote_type', display_name='DP Remote Type'),
        f.BoolField('ignore_ip', display_name='Ignore IP?'),
        f.StringField('info', display_name='Comments'),
        f.LinkField('jack', display_name='Jack', link_to='HorizontalCable'),
        f.StringField('jack_char', display_name='Jack(char)'),
        f.BoolField('loop_guard_enabled', display_name='Loop Guard?'),
        f.BoolField('monitored', display_name='Monitored?'),
        f.LinkField('monitorstatus', display_name='Monitored Status', link_to='MonitorStatus'),
        f.StringField('name', display_name='Name'),
        f.LinkField('neighbor', display_name='Neighbor', link_to='Interface'),
        f.BoolField('neighbor_fixed', display_name='Neighbor Fixed?'),
        f.IntegerField('neighbor_missed', display_name='Neighbor Missed'),
        f.StringField('number', display_name='Number'),
        f.StringField('oper_duplex', display_name='Oper Duplex'),
        f.StringField('oper_status', display_name='Oper Status'),
        f.BoolField('overwrite_descr', display_name='Overwrite Description?'),
        f.LinkField('physaddr', display_name='Physical (MAC) Address', link_to='PhysAddr'),
        f.StringField('room_char', display_name='Room(char)'),
        f.BoolField('root_guard_enabled', display_name='Root Guard?'),
        f.BoolField('snmp_managed', display_name='SNMP-Managed?'),
        f.IntegerField('speed', display_name='Speed'),
        f.StringField('stp_id', display_name='STP Port ID'),
        f.StringField('type', display_name='Type'),
    ]
    _views = {'all': ['number', 'name', 'device', 'doc_status', 'jack', 'jack_char', 'room_char', 'circuit', 'dlci', 'description', 'overwrite_descr', 'type', 'speed', 'admin_duplex', 'oper_duplex', 'admin_status', 'auto_dns', 'oper_status', 'monitored', 'monitorstatus', 'snmp_managed', 'physaddr', 'neighbor', 'neighbor_fixed', 'neighbor_missed', 'stp_id', 'bpdu_filter_enabled', 'bpdu_guard_enabled', 'loop_guard_enabled', 'root_guard_enabled', 'ignore_ip', 'dp_remote_id', 'dp_remote_ip', 'dp_remote_port', 'dp_remote_type', 'down_from', 'down_until', 'contactlist', 'info'], 'brief': ['number', 'name', 'device', 'jack', 'description', 'neighbor']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'device']])
        return l.strip()

    def arp_entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(interface=self.id)

    def fwt_entries(self):
        cls = getattr(pynetdot.models, 'FWTableEntry')
        return cls.search(interface=self.id)

    def neighbors(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(neighbor=self.id)

    def vlans(self):
        cls = getattr(pynetdot.models, 'InterfaceVlan')
        return cls.search(interface=self.id)

    def ips(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(interface=self.id)


class BaseInterfaceVlan(n.Netdot):
    resource = 'InterfaceVlan/'
    id_field = 'id'
    _fields = [
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.StringField('stp_des_bridge', display_name='STP Des. Bridge'),
        f.StringField('stp_des_port', display_name='STP Des. Port'),
        f.LinkField('stp_instance', display_name='STP Instance', link_to='STPInstance'),
        f.StringField('stp_state', display_name='STP State'),
        f.LinkField('vlan', display_name='Vlan', link_to='Vlan'),
    ]
    _views = {'all': ['interface', 'vlan', 'stp_instance', 'stp_des_bridge', 'stp_des_port', 'stp_state'], 'brief': ['interface', 'vlan', 'stp_instance', 'stp_des_bridge', 'stp_des_port', 'stp_state']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['interface', 'vlan']])
        return l.strip()


class BaseIpblock(n.Netdot):
    resource = 'Ipblock/'
    id_field = 'id'
    _fields = [
        f.StringField('address', display_name='Address'),
        f.StringField('description', display_name='Description'),
        f.DateTimeField('first_seen', display_name='First Seen'),
        f.StringField('info', display_name='Comments'),
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.DateTimeField('last_seen', display_name='Last Seen'),
        f.LinkField('owner', display_name='Owner', link_to='Entity'),
        f.LinkField('parent', display_name='Parent', link_to='Ipblock'),
        f.IntegerField('prefix', display_name='Prefix Length'),
        f.LinkField('status', display_name='Status', link_to='IpblockStatus'),
        f.BoolField('use_network_broadcast', display_name='Use Network/Broadcast?'),
        f.LinkField('used_by', display_name='Used by', link_to='Entity'),
        f.IntegerField('version', display_name='Version(4/6)'),
        f.LinkField('vlan', display_name='Vlan', link_to='Vlan'),
    ]
    _views = {'address_brief': ['address', 'status', 'used_by', 'description', 'last_seen'], 'all': ['address', 'prefix', 'version', 'parent', 'interface', 'vlan', 'status', 'owner', 'used_by', 'description', 'first_seen', 'last_seen', 'use_network_broadcast', 'info'], 'brief': ['address', 'prefix', 'status', 'used_by', 'description', 'last_seen'], 'subnet_brief': ['address', 'prefix', 'status', 'vlan', 'used_by', 'description'], 'container_brief': ['address', 'prefix', 'status', 'owner', 'used_by', 'description']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['address', 'prefix']])
        return l.strip()

    def arp_entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(ipaddr=self.id)

    def snmp_devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(snmp_target=self.id)

    def dhcp_scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(ipblock=self.id)

    def services(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(ip=self.id)

    def children(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(parent=self.id)

    def attributes(self):
        cls = getattr(pynetdot.models, 'IpblockAttr')
        return cls.search(ipblock=self.id)

    def a_records(self):
        cls = getattr(pynetdot.models, 'RRADDR')
        return cls.search(ipblock=self.id)

    def ptr_records(self):
        cls = getattr(pynetdot.models, 'RRPTR')
        return cls.search(ipblock=self.id)

    def sites(self):
        cls = getattr(pynetdot.models, 'SiteSubnet')
        return cls.search(subnet=self.id)

    def zones(self):
        cls = getattr(pynetdot.models, 'SubnetZone')
        return cls.search(subnet=self.id)


class BaseIpblockAttr(n.Netdot):
    resource = 'IpblockAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('ipblock', display_name='Ipblock', link_to='Ipblock'),
        f.LinkField('name', display_name='Name', link_to='IpblockAttrName'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'ipblock'], 'brief': ['name', 'value', 'ipblock']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value', 'ipblock']])
        return l.strip()


class BaseIpblockAttrName(n.Netdot):
    resource = 'IpblockAttrName/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def attributes(self):
        cls = getattr(pynetdot.models, 'IpblockAttr')
        return cls.search(name=self.id)


class BaseIpblockStatus(n.Netdot):
    resource = 'IpblockStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('name', display_name=''),
    ]
    _views = {'all': ['name'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def ipblocks(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(status=self.id)


class BaseIpService(n.Netdot):
    resource = 'IpService/'
    id_field = 'id'
    _fields = [
        f.LinkField('contactlist', display_name='', link_to='ContactList'),
        f.LinkField('ip', display_name='', link_to='Ipblock'),
        f.BoolField('monitored', display_name=''),
        f.LinkField('monitorstatus', display_name='', link_to='MonitorStatus'),
        f.LinkField('service', display_name='', link_to='Service'),
    ]
    _views = {'all': ['ip', 'service', 'monitored', 'monitorstatus', 'contactlist'], 'brief': ['ip', 'service']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['ip', 'service']])
        return l.strip()


class BaseMaintContract(n.Netdot):
    resource = 'MaintContract/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('number', display_name='Number'),
        f.LinkField('provider', display_name='Provider', link_to='Entity'),
    ]
    _views = {'all': ['number', 'provider', 'info'], 'brief': ['number']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['provider', 'number']])
        return l.strip()

    def assets(self):
        cls = getattr(pynetdot.models, 'Asset')
        return cls.search(maint_contract=self.id)


class BaseMonitorStatus(n.Netdot):
    resource = 'MonitorStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Status'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def bgppeers(self):
        cls = getattr(pynetdot.models, 'BGPPeering')
        return cls.search(monitorstatus=self.id)

    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(monitorstatus=self.id)

    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(monitorstatus=self.id)

    def ipservices(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(monitorstatus=self.id)


class BaseOUI(n.Netdot):
    resource = 'OUI/'
    id_field = 'id'
    _fields = [
        f.StringField('oui', display_name='OUI'),
        f.StringField('vendor', display_name='Vendor'),
    ]
    _views = {'all': ['oui', 'vendor'], 'brief': ['oui', 'vendor']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['oui', 'vendor']])
        return l.strip()


class BasePerson(n.Netdot):
    resource = 'Person/'
    id_field = 'id'
    _fields = [
        f.StringField('aliases', display_name='Aliases'),
        f.StringField('cell', display_name='Cell Phone'),
        f.StringField('email', display_name='Email'),
        f.StringField('emailpager', display_name='Pager Email'),
        f.LinkField('entity', display_name='Employer', link_to='Entity'),
        f.IntegerField('extension', display_name='Work Phone Extension'),
        f.StringField('fax', display_name='Fax'),
        f.StringField('firstname', display_name='First Name'),
        f.StringField('home', display_name='Home Phone'),
        f.StringField('info', display_name='Comments'),
        f.StringField('lastname', display_name='Last Name'),
        f.LinkField('location', display_name='Site', link_to='Site'),
        f.StringField('office', display_name='Work Phone'),
        f.StringField('pager', display_name='Pager'),
        f.StringField('password', display_name='Password'),
        f.StringField('position', display_name='Position'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.LinkField('user_type', display_name='User Type', link_to='UserType'),
        f.StringField('username', display_name='Username'),
    ]
    _views = {'all': ['firstname', 'lastname', 'aliases', 'username', 'password', 'user_type', 'position', 'entity', 'location', 'room', 'email', 'office', 'extension', 'cell', 'home', 'pager', 'emailpager', 'fax', 'info'], 'brief': ['firstname', 'lastname', 'office', 'entity']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['lastname', 'firstname']])
        return l.strip()

    def roles(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(person=self.id)


class BasePhysAddr(n.Netdot):
    resource = 'PhysAddr/'
    id_field = 'id'
    _fields = [
        f.StringField('address', display_name='Address'),
        f.DateTimeField('first_seen', display_name='First Seen'),
        f.DateTimeField('last_seen', display_name='Last Seen'),
        f.BoolField('static', display_name='Static?'),
    ]
    _views = {'all': ['address', 'static', 'first_seen', 'last_seen'], 'brief': ['address', 'static', 'first_seen', 'last_seen']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['address']])
        return l.strip()

    def arp_entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(physaddr=self.id)

    def assets(self):
        cls = getattr(pynetdot.models, 'Asset')
        return cls.search(physaddr=self.id)

    def dhcp_hosts(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(physaddr=self.id)

    def fwt_entries(self):
        cls = getattr(pynetdot.models, 'FWTableEntry')
        return cls.search(physaddr=self.id)

    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(physaddr=self.id)

    def attributes(self):
        cls = getattr(pynetdot.models, 'PhysAddrAttr')
        return cls.search(physaddr=self.id)


class BasePhysAddrAttr(n.Netdot):
    resource = 'PhysAddrAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('name', display_name='Name', link_to='PhysAddrAttrName'),
        f.LinkField('physaddr', display_name='Physical Address', link_to='PhysAddr'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'physaddr'], 'brief': ['name', 'value', 'physaddr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value', 'physaddr']])
        return l.strip()


class BasePhysAddrAttrName(n.Netdot):
    resource = 'PhysAddrAttrName/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def attributes(self):
        cls = getattr(pynetdot.models, 'PhysAddrAttr')
        return cls.search(name=self.id)


class BaseProduct(n.Netdot):
    resource = 'Product/'
    id_field = 'id'
    _fields = [
        f.StringField('config_type', display_name='Config Type'),
        f.StringField('description', display_name='Description'),
        f.StringField('info', display_name='Comments'),
        f.StringField('latest_os', display_name='Recommended OS'),
        f.LinkField('manufacturer', display_name='Manufacturer', link_to='Entity'),
        f.StringField('name', display_name='Name'),
        f.StringField('part_number', display_name='Part Number'),
        f.StringField('sysobjectid', display_name='System ID'),
        f.LinkField('type', display_name='Type', link_to='ProductType'),
    ]
    _views = {'all': ['name', 'type', 'description', 'sysobjectid', 'manufacturer', 'config_type', 'part_number', 'latest_os', 'info'], 'brief': ['name', 'type', 'description', 'manufacturer']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['manufacturer', 'name']])
        return l.strip()

    def assets(self):
        cls = getattr(pynetdot.models, 'Asset')
        return cls.search(product_id=self.id)


class BaseProductType(n.Netdot):
    resource = 'ProductType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def products(self):
        cls = getattr(pynetdot.models, 'Product')
        return cls.search(type=self.id)


class BaseRoom(n.Netdot):
    resource = 'Room/'
    id_field = 'id'
    _fields = [
        f.LinkField('floor', display_name='Floor', link_to='Floor'),
        f.StringField('name', display_name='Number'),
    ]
    _views = {'all': ['name', 'floor'], 'brief': ['name', 'floor']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['floor', 'name']])
        return l.strip()

    def closets(self):
        cls = getattr(pynetdot.models, 'Closet')
        return cls.search(room=self.id)

    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(room=self.id)

    def jacks(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(room=self.id)

    def people(self):
        cls = getattr(pynetdot.models, 'Person')
        return cls.search(room=self.id)


class BaseRR(n.Netdot):
    resource = 'RR/'
    id_field = 'id'
    _fields = [
        f.BoolField('active', display_name='Active?'),
        f.BoolField('auto_update', display_name='Auto Update?'),
        f.DateTimeField('created', display_name='Created'),
        f.DateField('expiration', display_name='Expiration Date'),
        f.StringField('info', display_name='Comments'),
        f.DateTimeField('modified', display_name='Modified'),
        f.StringField('name', display_name='Name'),
        f.LinkField('zone', display_name='Zone', link_to='Zone'),
    ]
    _views = {'all': ['name', 'zone', 'active', 'auto_update', 'created', 'modified', 'expiration', 'info'], 'brief': ['name', 'zone']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'zone']])
        return l.strip()

    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(name=self.id)

    def a_records(self):
        cls = getattr(pynetdot.models, 'RRADDR')
        return cls.search(rr=self.id)

    def cnames(self):
        cls = getattr(pynetdot.models, 'RRCNAME')
        return cls.search(rr=self.id)

    def ds_records(self):
        cls = getattr(pynetdot.models, 'RRDS')
        return cls.search(rr=self.id)

    def hinfo_records(self):
        cls = getattr(pynetdot.models, 'RRHINFO')
        return cls.search(rr=self.id)

    def loc_records(self):
        cls = getattr(pynetdot.models, 'RRLOC')
        return cls.search(rr=self.id)

    def mx_records(self):
        cls = getattr(pynetdot.models, 'RRMX')
        return cls.search(rr=self.id)

    def naptr_records(self):
        cls = getattr(pynetdot.models, 'RRNAPTR')
        return cls.search(rr=self.id)

    def ns_records(self):
        cls = getattr(pynetdot.models, 'RRNS')
        return cls.search(rr=self.id)

    def ptr_records(self):
        cls = getattr(pynetdot.models, 'RRPTR')
        return cls.search(rr=self.id)

    def srv_records(self):
        cls = getattr(pynetdot.models, 'RRSRV')
        return cls.search(rr=self.id)

    def txt_records(self):
        cls = getattr(pynetdot.models, 'RRTXT')
        return cls.search(rr=self.id)


class BaseRRADDR(n.Netdot):
    resource = 'RRADDR/'
    id_field = 'id'
    _fields = [
        f.LinkField('ipblock', display_name='Ipblock', link_to='Ipblock'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['ipblock', 'rr', 'ttl'], 'brief': ['rr', 'ipblock']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['ipblock', 'rr']])
        return l.strip()


class BaseRRCNAME(n.Netdot):
    resource = 'RRCNAME/'
    id_field = 'id'
    _fields = [
        f.StringField('cname', display_name='CNAME'),
        f.LinkField('rr', display_name='Alias', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['rr', 'cname', 'ttl'], 'brief': ['rr', 'cname']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'cname']])
        return l.strip()


class BaseRRDS(n.Netdot):
    resource = 'RRDS/'
    id_field = 'id'
    _fields = [
        f.IntegerField('algorithm', display_name='Algorithm'),
        f.StringField('digest', display_name='Digest'),
        f.IntegerField('digest_type', display_name='Digest Type'),
        f.IntegerField('key_tag', display_name='Key Tag'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['rr', 'ttl', 'key_tag', 'algorithm', 'digest_type', 'digest'], 'brief': ['rr', 'ttl', 'key_tag', 'algorithm', 'digest_type', 'digest']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'key_tag']])
        return l.strip()


class BaseRRHINFO(n.Netdot):
    resource = 'RRHINFO/'
    id_field = 'id'
    _fields = [
        f.StringField('cpu', display_name='CPU'),
        f.StringField('os', display_name='OS'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['cpu', 'os', 'rr', 'ttl'], 'brief': ['cpu', 'os', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['cpu', 'os', 'rr']])
        return l.strip()


class BaseRRLOC(n.Netdot):
    resource = 'RRLOC/'
    id_field = 'id'
    _fields = [
        f.IntegerField('altitude', display_name='Altitude'),
        f.StringField('horiz_pre', display_name='Horizontal Precision'),
        f.IntegerField('latitude', display_name='Latitude'),
        f.IntegerField('longitude', display_name='Longitude'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('size', display_name='Size'),
        f.StringField('ttl', display_name='TTL'),
        f.StringField('vert_pre', display_name='Vertical Precision'),
    ]
    _views = {'all': ['rr', 'size', 'horiz_pre', 'vert_pre', 'latitude', 'longitude', 'altitude'], 'brief': ['rr', 'latitude', 'longitude', 'altitude']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr']])
        return l.strip()


class BaseRRMX(n.Netdot):
    resource = 'RRMX/'
    id_field = 'id'
    _fields = [
        f.StringField('exchange', display_name='Exchange'),
        f.IntegerField('preference', display_name='Preference'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['preference', 'exchange', 'rr', 'ttl'], 'brief': ['preference', 'exchange', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['preference', 'exchange', 'rr']])
        return l.strip()


class BaseRRNAPTR(n.Netdot):
    resource = 'RRNAPTR/'
    id_field = 'id'
    _fields = [
        f.StringField('flags', display_name='Flags'),
        f.IntegerField('order_field', display_name='Order'),
        f.IntegerField('preference', display_name='Preference'),
        f.StringField('regexpr', display_name='Regexp'),
        f.StringField('replacement', display_name='Replacement'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('services', display_name='Services'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['order_field', 'preference', 'flags', 'services', 'regexpr', 'replacement', 'rr', 'ttl'], 'brief': ['rr', 'services', 'regexpr', 'replacement']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'services', 'regexpr', 'replacement']])
        return l.strip()


class BaseRRNS(n.Netdot):
    resource = 'RRNS/'
    id_field = 'id'
    _fields = [
        f.StringField('nsdname', display_name='Name Server'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['nsdname', 'rr', 'ttl'], 'brief': ['nsdname', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['nsdname', 'rr']])
        return l.strip()


class BaseRRPTR(n.Netdot):
    resource = 'RRPTR/'
    id_field = 'id'
    _fields = [
        f.LinkField('ipblock', display_name='IP', link_to='Ipblock'),
        f.StringField('ptrdname', display_name='Domain Name'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['rr', 'ipblock', 'ptrdname', 'ttl'], 'brief': ['rr', 'ipblock', 'ptrdname']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'ipblock', 'ptrdname']])
        return l.strip()


class BaseRRSRV(n.Netdot):
    resource = 'RRSRV/'
    id_field = 'id'
    _fields = [
        f.IntegerField('port', display_name='Port'),
        f.IntegerField('priority', display_name='Priority'),
        f.LinkField('rr', display_name='Name', link_to='RR'),
        f.StringField('target', display_name='Target'),
        f.StringField('ttl', display_name='TTL'),
        f.IntegerField('weight', display_name='Weight'),
    ]
    _views = {'all': ['rr', 'ttl', 'priority', 'weight', 'port', 'target'], 'brief': ['rr', 'priority', 'weight', 'port', 'target']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'target']])
        return l.strip()


class BaseRRTXT(n.Netdot):
    resource = 'RRTXT/'
    id_field = 'id'
    _fields = [
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
        f.StringField('txtdata', display_name='Text'),
    ]
    _views = {'all': ['txtdata', 'rr', 'ttl'], 'brief': ['txtdata', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['txtdata', 'rr']])
        return l.strip()


class BaseService(n.Netdot):
    resource = 'Service/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def Ips(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(service=self.id)


class BaseSite(n.Netdot):
    resource = 'Site/'
    id_field = 'id'
    _fields = [
        f.StringField('aliases', display_name='Aliases'),
        f.LinkField('availability', display_name='Availability', link_to='Availability'),
        f.StringField('city', display_name='City'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.StringField('country', display_name='Country'),
        f.IntegerField('gsf', display_name='GSF'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.StringField('number', display_name='Site ID'),
        f.StringField('pobox', display_name='P.O. Box'),
        f.StringField('state', display_name='State'),
        f.StringField('street1', display_name='Street (1)'),
        f.StringField('street2', display_name='Street (2)'),
        f.StringField('zip', display_name='Zip/Postal Code'),
    ]
    _views = {'all': ['name', 'number', 'gsf', 'aliases', 'street1', 'street2', 'pobox', 'city', 'state', 'zip', 'country', 'availability', 'contactlist', 'info'], 'brief': ['name', 'number', 'street1', 'city']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'aliases']])
        return l.strip()

    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(site=self.id)

    def entities(self):
        cls = getattr(pynetdot.models, 'EntitySite')
        return cls.search(site=self.id)

    def floors(self):
        cls = getattr(pynetdot.models, 'Floor')
        return cls.search(site=self.id)

    def people(self):
        cls = getattr(pynetdot.models, 'Person')
        return cls.search(location=self.id)

    def farlinks(self):
        cls = getattr(pynetdot.models, 'SiteLink')
        return cls.search(farend=self.id)

    def nearlinks(self):
        cls = getattr(pynetdot.models, 'SiteLink')
        return cls.search(nearend=self.id)

    def subnets(self):
        cls = getattr(pynetdot.models, 'SiteSubnet')
        return cls.search(site=self.id)


class BaseSiteLink(n.Netdot):
    resource = 'SiteLink/'
    id_field = 'id'
    _fields = [
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.LinkField('farend', display_name='Destination (Site)', link_to='Site'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.LinkField('nearend', display_name='Origin (Site)', link_to='Site'),
    ]
    _views = {'all': ['name', 'entity', 'nearend', 'farend', 'info'], 'brief': ['name', 'entity', 'nearend', 'farend']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(linkid=self.id)


class BaseSiteSubnet(n.Netdot):
    resource = 'SiteSubnet/'
    id_field = 'id'
    _fields = [
        f.LinkField('site', display_name='Site', link_to='Site'),
        f.LinkField('subnet', display_name='Subnet', link_to='Ipblock'),
    ]
    _views = {'all': ['subnet', 'site'], 'brief': ['subnet', 'site']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['subnet', 'site']])
        return l.strip()


class BaseSplice(n.Netdot):
    resource = 'Splice/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name=''),
        f.LinkField('strand1', display_name='', link_to='CableStrand'),
        f.LinkField('strand2', display_name='', link_to='CableStrand'),
    ]
    _views = {'all': ['strand1', 'strand2'], 'brief': ['strand1', 'strand2']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['strand1', 'strand2']])
        return l.strip()


class BaseSTPInstance(n.Netdot):
    resource = 'STPInstance/'
    id_field = 'id'
    _fields = [
        f.IntegerField('bridge_priority', display_name='Bridge Priority'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.IntegerField('number', display_name='Number'),
        f.StringField('root_bridge', display_name='Root Bridge'),
        f.IntegerField('root_port', display_name='Root Port'),
    ]
    _views = {'all': ['number', 'device', 'root_port', 'root_bridge', 'bridge_priority'], 'brief': ['number', 'device', 'root_port', 'root_bridge', 'bridge_priority']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['number', 'device']])
        return l.strip()

    def stp_ports(self):
        cls = getattr(pynetdot.models, 'InterfaceVlan')
        return cls.search(stp_instance=self.id)


class BaseStrandStatus(n.Netdot):
    resource = 'StrandStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name=''),
        f.StringField('name', display_name=''),
    ]
    _views = {'all': ['name'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(status=self.id)


class BaseSubnetZone(n.Netdot):
    resource = 'SubnetZone/'
    id_field = 'id'
    _fields = [
        f.LinkField('subnet', display_name='Subnet', link_to='Ipblock'),
        f.LinkField('zone', display_name='Zone', link_to='Zone'),
    ]
    _views = {'all': ['subnet', 'zone'], 'brief': ['subnet', 'zone']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['subnet', 'zone']])
        return l.strip()


class BaseVlan(n.Netdot):
    resource = 'Vlan/'
    id_field = 'id'
    _fields = [
        f.StringField('description', display_name='Description'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.IntegerField('vid', display_name='VLAN ID'),
        f.LinkField('vlangroup', display_name='Group', link_to='VlanGroup'),
    ]
    _views = {'all': ['vid', 'name', 'vlangroup', 'description', 'info'], 'brief': ['vid', 'name', 'description']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['vid']])
        return l.strip()

    def interfaces(self):
        cls = getattr(pynetdot.models, 'InterfaceVlan')
        return cls.search(vlan=self.id)

    def subnets(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(vlan=self.id)


class BaseVlanGroup(n.Netdot):
    resource = 'VlanGroup/'
    id_field = 'id'
    _fields = [
        f.StringField('description', display_name='Description'),
        f.IntegerField('end_vid', display_name='End'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.IntegerField('start_vid', display_name='Start'),
    ]
    _views = {'all': ['name', 'start_vid', 'end_vid', 'description', 'info'], 'brief': ['name', 'description', 'start_vid', 'end_vid']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def vlans(self):
        cls = getattr(pynetdot.models, 'Vlan')
        return cls.search(vlangroup=self.id)


class BaseZone(n.Netdot):
    resource = 'Zone/'
    id_field = 'id'
    _fields = [
        f.BoolField('active', display_name='Active?'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.IntegerField('default_ttl', display_name='Default TTL'),
        f.IntegerField('expire', display_name='Expire'),
        f.StringField('export_file', display_name='Export File'),
        f.StringField('include', display_name='Include'),
        f.StringField('info', display_name='Comments'),
        f.IntegerField('minimum', display_name='Minimum'),
        f.StringField('mname', display_name='Server Name'),
        f.StringField('name', display_name='Domain Name'),
        f.IntegerField('refresh', display_name='Refresh'),
        f.IntegerField('retry', display_name='Retry'),
        f.StringField('rname', display_name='Mail Box'),
        f.IntegerField('serial', display_name='Serial'),
    ]
    _views = {'all': ['name', 'mname', 'rname', 'serial', 'refresh', 'retry', 'expire', 'minimum', 'contactlist', 'active', 'export_file', 'default_ttl', 'include', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    def records(self):
        cls = getattr(pynetdot.models, 'RR')
        return cls.search(zone=self.id)

    def subnets(self):
        cls = getattr(pynetdot.models, 'SubnetZone')
        return cls.search(zone=self.id)

    def aliases(self):
        cls = getattr(pynetdot.models, 'ZoneAlias')
        return cls.search(zone=self.id)


class BaseZoneAlias(n.Netdot):
    resource = 'ZoneAlias/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Domain Name'),
        f.LinkField('zone', display_name='Zone', link_to='Zone'),
    ]
    _views = {'all': ['name', 'zone', 'info'], 'brief': ['name', 'zone']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()



