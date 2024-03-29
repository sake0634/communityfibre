from django.contrib import admin
from .models import Node,Port,Service,Sap,SdpBinding,Sdp

# Register your models here.
#admin.site.register(Node,Port,Service,Sap,SdpBinding,Sdp)
""" class PortInline(admin.TabularInline):
    model = Port
    extra = 1 """

class NodeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['node_name']}),
        ('System Ip', {'fields': ['system_ip']}),
    ]
    #inlines = [PortInline]

    list_display = ('node_name', 'system_ip')
    search_fields = ['node_name']

admin.site.register(Node,NodeAdmin)



class PortAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Port Name",{'fields':['port_name']}),
        ("Node",{'fields':['node_id']})
    ]

    list_display = ('port_name','node_id')
    search_fields = ['port_name']

admin.site.register(Port,PortAdmin)

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Service ID",{'fields':['service_id_str']}),
        ("Node",{'fields':['node_id']})
    ]

    list_display = ('service_id_str','node_id')
    search_fields = ['service_id_str']

admin.site.register(Service,ServiceAdmin)

class SdpAdmin(admin.ModelAdmin):
    fieldsets = [
        ("From Node",{'fields':['from_node']}),
        ("To Node",{'fields':['to_node']}),
        ("ID",{'fields':['id']}),
    ]

    list_display = ('from_node','to_node','id')
    search_fields = ['from_node','to_node']

admin.site.register(Sdp,SdpAdmin)

class SapAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Service Id",{'fields':['service_id']}),
        ("Port",{'fields':['port']}),
        ("Outer Vlan",{'fields':['outer_vlan']}),
        ("Inner Vlan",{'fields':['inner_vlan']}),
    ]

    list_display = ('service_id','port','outer_vlan','inner_vlan')

admin.site.register(Sap,SapAdmin)

class SdpBindingAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Service Id",{'fields':['service']}),
        ("Sdp Tunnel",{'fields':['sdp_id']}),
        ("VcId",{'fields':['vc_id']}),
    ]

    list_display = ('service','sdp_id','vc_id')

admin.site.register(SdpBinding,SdpBindingAdmin)