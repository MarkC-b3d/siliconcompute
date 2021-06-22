import bpy

preferences = bpy.context.preferences.addons['cycles'].preferences
for device_type in preferences.get_device_types(bpy.context):
    preferences.get_devices_for_type(device_type[0])
for device in preferences.devices:
    print('Device {} of type {} found'.format(
        device.name, device.type))
    if device.type:
        'OPTIX'
        print("Optix Device detected using Optix")
        bpy.context.preferences.addons[
            "cycles"
        ].preferences.compute_device_type = "OPTIX"
    elif device.type:
        'CUDA'
        print("CUDA Device detected using CUDA")
        bpy.context.preferences.addons[
            "cycles"
        ].preferences.compute_device_type = "CUDA"
    elif device.type:
        'OPENCL'
        print("OpenCL Device detected using OpenCL")
        bpy.context.preferences.addons[
            "cycles"
        ].preferences.compute_device_type = "OPENCL"
