def getSystemInfo(cls):
    system = {
        'boot_time': psutil.boot_time(),
        'cpu_count': psutil.cpu_count(),
        'cpu_stats': psutil.cpu_stats().__dict__,
        'cpu_times': [k.__dict__ for k in psutil.cpu_times(percpu=True)],
        'disk_io_counters': psutil.disk_io_counters().__dict__,
        'disk_usage': [],
        'net_io_counters': psutil.net_io_counters().__dict__,
        'swap_memory': psutil.swap_memory().__dict__,
        'virtual_memory': psutil.virtual_memory().__dict__
    }

    partitions = psutil.disk_partitions()
    for p in partitions:
        if p.mountpoint in cls.INCLUDED_PARTITIONS:
            usage = psutil.disk_usage(p.mountpoint)
            system['disk_usage'].append({
                'mountpoint': p.mountpoint,
                'total': usage.total,
                'used': usage.used
            })

    return system

