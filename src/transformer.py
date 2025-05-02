def transform(raw_data):
    full_name = f"{raw_data['name']} {raw_data['surname']}"
    full_ip = f"{raw_data['ip_address']}:{raw_data['port']}"
    return {
        'id': raw_data['id'],
        'full_name': full_name,
        'birthdate': raw_data['birthdate'],
        'full_ip': full_ip,
        'timestamp': raw_data['timestamp']
    }
