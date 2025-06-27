import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import folium  
from folium import plugins
from branca.colormap import linear 

FILENAME = 'test_log19.txt'

def parse_data_line(line): 
    parts = [p.strip() for p in line.replace(',', ' ').split()]
    try:
        numbers = [float(p) for p in parts]
        return numbers if 1 <= len(numbers) <= 30 else None
    except ValueError:
        return None    
    
def parse_imu_vector(line, start):  
    vector = line[start:].replace('(', '').replace(')', '').strip()
    parts = vector.split(',') 
    vals = [float(p) for p in parts] 
    return vals

def parse_IMU_line(line):   
    start = line.find(':') +  1 
    if 'Temperature' in line: 
        end = line.find(' degrees', start)  
        temp = float(line[start:end])  
        return temp, 'temp'  
    
    if 'Accelerometer' in line:   
        acc = parse_imu_vector(line, start) 
        return acc[0], acc[1], acc[2], 'acc'  
    
    if 'Magnetometer' in line:
        mag = parse_imu_vector(line, start) 
        return mag[0], mag[1], mag[2], 'mag' 
    
    if 'Gyroscope' in line:
        gyro = parse_imu_vector(line, start) 
        return gyro[0], gyro[1], gyro[2], 'gyro' 
    
    if 'Euler angle' in line:
        euler = parse_imu_vector(line, start) 
        return euler[0], euler[1], euler[2], 'euler' 
    
    if 'Quaternion' in line:
        quat = parse_imu_vector(line, start) 
        return quat[0], quat[1], quat[2], quat[3], 'quat' 
    
    if 'Linear acceleration' in line:
        lin_acc = parse_imu_vector(line, start) 
        return lin_acc[0], lin_acc[1], lin_acc[2], 'lin_acc' 
    
    if 'Gravity' in line:
        grav = parse_imu_vector(line, start) 
        return grav[0], grav[1], grav[2], 'grav' 
    
    return None

def parse_file(path): 
    data = {}   
    # Data line for bmp280, SCD41, and GPS 
    data['bmp280_temp'] = [] 
    data['bmp280_pressure'] = []
    data['bmp280_alt'] = []
    data['scd_co2'] = []
    data['scd_temp'] = []
    data['scd_humidity'] = []
    data['gps_lat'] = []
    data['gps_long'] = []
    data['gps_alt'] = []
    data['time'] = []  
    # Data From the IMU, BNO055 
    data['imu_temp'] = []  

    data['imu_acc_x'] = []
    data['imu_acc_y'] = []
    data['imu_acc_z'] = [] 

    data['imu_mag_x'] = []
    data['imu_mag_y'] = []
    data['imu_mag_z'] = [] 

    data['imu_gyro_x'] = []
    data['imu_gyro_y'] = []
    data['imu_gyro_z'] = []   

    data['imu_euler_x'] = [] 
    data['imu_euler_y'] = []
    data['imu_euler_z'] = []
    
    data['imu_quat_w'] = []
    data['imu_quat_x'] = []
    data['imu_quat_y'] = []
    data['imu_quat_z'] = []     

    data['imu_lin_acc_x'] = []
    data['imu_lin_acc_y'] = []
    data['imu_lin_acc_z'] = [] 

    data['imu_grav_x'] = []
    data['imu_grav_y'] = []
    data['imu_grav_z'] = [] 

    with open(path, 'r') as file: 
        for i, line in enumerate(file): 
            if line and (line[0].isdigit() or line[0] == '-' or line[0] == '.'):
                numbers = parse_data_line(line) 
                if numbers:
                    data['bmp280_temp'].append(numbers[0])
                    data['bmp280_pressure'].append(numbers[1])
                    data['bmp280_alt'].append(numbers[2])
                    data['scd_co2'].append(numbers[3])
                    data['scd_temp'].append(numbers[4])
                    data['scd_humidity'].append(numbers[5])
                    data['gps_lat'].append(numbers[6])
                    data['gps_long'].append(numbers[7])
                    data['time'].append(numbers[-1]) 
                    if len(numbers) > 9: 
                        data['gps_alt'].append(numbers[8]) 
                    else:  
                        data['gps_alt'].append(0.0) 
            elif line: 
                vals = parse_IMU_line(line)  
                if vals[-1] == 'temp': 
                    data['imu_temp'].append(vals[0])
                elif vals[-1] == 'acc':
                    data['imu_acc_x'].append(vals[0])
                    data['imu_acc_y'].append(vals[1])
                    data['imu_acc_z'].append(vals[2])
                elif vals[-1] == 'mag':
                    data['imu_mag_x'].append(vals[0])
                    data['imu_mag_y'].append(vals[1])
                    data['imu_mag_z'].append(vals[2])
                elif vals[-1] == 'gyro':
                    data['imu_gyro_x'].append(vals[0])
                    data['imu_gyro_y'].append(vals[1])
                    data['imu_gyro_z'].append(vals[2])
                elif vals[-1] == 'euler':
                    data['imu_euler_x'].append(vals[0])
                    data['imu_euler_y'].append(vals[1])
                    data['imu_euler_z'].append(vals[2])
                elif vals[-1] == 'quat': 
                    data['imu_quat_w'].append(vals[0])
                    data['imu_quat_x'].append(vals[1])
                    data['imu_quat_y'].append(vals[2])
                    data['imu_quat_z'].append(vals[3])
                elif vals[-1] == 'lin_acc': 
                    data['imu_lin_acc_x'].append(vals[0])
                    data['imu_lin_acc_y'].append(vals[1])
                    data['imu_lin_acc_z'].append(vals[2]) 
                elif vals[-1] == 'grav':
                    data['imu_grav_x'].append(vals[0])
                    data['imu_grav_y'].append(vals[1])
                    data['imu_grav_z'].append(vals[2])
            else: 
                print(f"Skipping empty line {i+1}")   
    return data

def plot_data(data, x, ys, x_label='X-axis', y_label='Y-axis', title='Weather Balloon Data', save_path=None):  
    plt.figure(figsize=(10, 6)) 
    for y in ys: 
        plt.scatter(data[x], data[y], label=y, s=10)  
    plt.xlabel(x_label) 
    plt.ylabel(y_label)
    plt.title(title) 
    plt.legend()
    plt.grid() 

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Plot saved to {save_path}") 

    plt.show() 
    


FILENAME_PATH = 'data/' + FILENAME 
data = parse_file(FILENAME_PATH)  

plot_data(data, 'time', ['bmp280_temp', 'scd_temp', 'imu_temp'],
          x_label='Time (s)', y_label='Temperature (C)', title='Temperature Data', save_path='data/temperature_plot' + FILENAME +'.png')  

plot_data(data, 'bmp280_pressure', ['bmp280_alt', 'gps_alt'], x_label='Pressure (hPa)',
          y_label='Altitude (m)', title='Pressure vs Altitude', save_path='data/pressure_v_altitude_plot' + FILENAME +'.png') 

plot_data(data, 'time', ['scd_co2'], x_label='Time (s)', y_label='CO₂ Concentration (ppm)',
          title='CO₂ Concentration Over Time', save_path='data/c02_v_time' + FILENAME +'.png') 

plot_data(data, 'time', ['scd_humidity'], x_label='Time (s)', y_label='Humidity (%)',
          title='Humidity Over Time', save_path='data/humitity_v_time' + FILENAME +'.png') 

plot_data(data, 'time', ['imu_lin_acc_x', 'imu_lin_acc_y', 'imu_lin_acc_z'],
          x_label='Time (s)', y_label='Acceleration (m/s²)', title='IMU Linear Acceleration Data') 

# PLOT GPS path with recorded scatter points
valid_coords = [(lat, lon) for lat, lon in zip(data['gps_lat'], data['gps_long']) if lat != 0 and lon != 0]

if not valid_coords:
    print("❌ No valid GPS coordinates to plot.")
else:
    start_location = valid_coords[0]
    fmap = folium.Map(location=start_location, zoom_start=14)

    # Draw path
    folium.PolyLine(valid_coords, color="blue", weight=3).add_to(fmap)

    # Add recorded points as scatter (small transparent circles)
    for lat, lon in valid_coords:
        folium.CircleMarker(
            location=(lat, lon),
            radius=2,
            color='black',
            fill=True,
            fill_color='black',
            fill_opacity=0.6
        ).add_to(fmap)

    # Start and end markers
    folium.Marker(valid_coords[0], popup="Start", icon=folium.Icon(color="green")).add_to(fmap)
    folium.Marker(valid_coords[-1], popup="End", icon=folium.Icon(color="red")).add_to(fmap)

    # Save to HTML
    fmap.save("data/gps_path_map" + FILENAME + ".html")
    print("✅ Map with scatter points saved to gps_path_map.html")

gps_points = [
    (lat, lon, co2) for lat, lon, co2 in zip(data['gps_lat'], data['gps_long'], data['scd_co2'])
    if lat != 0 and lon != 0 and not pd.isna(co2)
]

if not gps_points:
    print("❌ No valid GPS or CO₂ data to plot.")
else:
    # Unpack points
    lats, lons, co2_vals = zip(*gps_points)

    # Initialize map centered on first point
    fmap_co2 = folium.Map(location=[lats[0], lons[0]], zoom_start=14)

    # Create color scale
    colormap = linear.YlOrRd_09.scale(min(co2_vals), max(co2_vals))
    colormap.caption = 'CO₂ Concentration (ppm)'
    fmap_co2.add_child(colormap)

    # Plot points with color by CO₂
    for lat, lon, co2 in gps_points:
        folium.CircleMarker(
            location=(lat, lon),
            radius=4,
            color=colormap(co2),
            fill=True,
            fill_color=colormap(co2),
            fill_opacity=0.8,
            popup=f"CO₂: {co2:.1f} ppm"
        ).add_to(fmap_co2)

    # Start and end markers
    folium.Marker([lats[0], lons[0]], popup="Start", icon=folium.Icon(color="green")).add_to(fmap_co2)
    folium.Marker([lats[-1], lons[-1]], popup="End", icon=folium.Icon(color="red")).add_to(fmap_co2)

    # Save map
    fmap_co2.save("data/gps_co2_map" + FILENAME + ".html")
    print("✅ CO₂-colored map saved to gps_co2_map.html") 

coords_humidity = [
    (lat, lon, hum)
    for lat, lon, hum in zip(data['gps_lat'], data['gps_long'], data['scd_humidity'])
    if lat != 0 and lon != 0
]

if coords_humidity:
    fmap_hum = folium.Map(location=[coords_humidity[0][0], coords_humidity[0][1]], zoom_start=12)

    # Create colormap
    humidity_vals = [hum for _, _, hum in coords_humidity]
    colormap_h = linear.YlGnBu_09.scale(min(humidity_vals), max(humidity_vals))
    colormap_h.caption = 'SCD Humidity (%)'
    colormap_h.add_to(fmap_hum)

    for lat, lon, hum in coords_humidity:
        folium.CircleMarker(
            location=[lat, lon],
            radius=4,
            fill=True,
            fill_opacity=0.8,
            color=colormap_h(hum),
            popup=f'Humidity: {hum:.2f}%'
        ).add_to(fmap_hum)

    fmap_hum.save("data/gps_humidity_map" + FILENAME + ".html")
    print("✅ Humidity map saved to gps_humidity_map.html")
else:
    print("❌ No valid GPS data for humidity mapping.")







