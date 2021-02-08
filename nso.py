import ncs
with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
    root = ncs.maagic.get_root(t)
    deviceconfig = root.devices.device["csr1"].config
    #deviceconfig.ios__native.ip.domain.name = 'test'
    #t.apply()


    print( dir(deviceconfig.ios__native.domain ))

