import tkinter as tk


def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal_degrees *= -1
    return decimal_degrees


def decimal_to_dms(decimal):
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = ((decimal - degrees) * 60 - minutes) * 60
    return degrees, minutes, seconds


def convert_coordinates_1():
    lat_degrees = float(entry_lat_degrees.get())
    lat_minutes = float(entry_lat_minutes.get())
    lat_seconds = float(entry_lat_seconds.get())
    lat_direction = variable_north_and_south.get()

    lon_degrees = float(entry_lon_degrees.get())
    lon_minutes = float(entry_lon_minutes.get())
    lon_seconds = float(entry_lon_seconds.get())
    lon_direction = variable_east_or_west.get()

    # Convert latitude and longitude from DMS to decimal
    latitude_decimal_1 = dms_to_decimal(lat_degrees, lat_minutes, lat_seconds, lat_direction)
    longitude_decimal_1 = dms_to_decimal(lon_degrees, lon_minutes, lon_seconds, lon_direction)

    # Update decimal coordinates labels
    decimal_latitude_text_1.set("{:.9f}".format(latitude_decimal_1))
    decimal_longitude_text_1.set("{:.9f}".format(longitude_decimal_1))


def convert_coordinates_2():
    # Get input values for latitude and longitude
    latitude_decimal = float(entry_lat_latitude.get())
    longitude_decimal = float(entry_lat_longitude.get())

    # Convert latitude
    lat_deg = int(latitude_decimal)
    lat_min = int(abs(latitude_decimal - lat_deg) * 60)
    lat_sec = int(((abs(latitude_decimal - lat_deg) * 60) - lat_min) * 60 * 100)  # Convert seconds to four digits
    if lat_deg >= 0:
        lat_direction = "N"
    else:
        lat_direction = "S"
        lat_deg = abs(lat_deg)

    # Convert longitude
    lon_deg = int(longitude_decimal)
    lon_min = int(abs(longitude_decimal - lon_deg) * 60)
    lon_sec = int(((abs(longitude_decimal - lon_deg) * 60) - lon_min) * 60 * 100)  # Convert seconds to four digits
    if lon_deg >= 0:
        lon_direction = "E"
    else:
        lon_direction = "W"
        lon_deg = abs(lon_deg)

    # Format the output result
    formatted_lat = f"{lat_direction}{lat_deg:02d}{lat_min:02d}{lat_sec:04d}"
    formatted_lon = f"{lon_direction}{lon_deg:03d}{lon_min:02d}{lon_sec:04d}"

    # Update the result display
    decimal_latitude_text.set(formatted_lat)
    decimal_longitude_text.set(formatted_lon)


def copy_to_clipboard(text):
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()


# 创建GUI窗口
window = tk.Tk()
window.title("Latitude/Longitude Unit Converter For X-Plane  V1.0")

# 创建标签（度分秒转十进制）
label_title = tk.Label(window, text="Degree-Minute-Second Coordinate Conversion to Decimal Coordinate：")
label_title.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

# 创建标签、输入框和按钮（纬度部分）
label_latitude = tk.Label(window, text="Latitude：")
label_latitude.grid(row=1, column=0, padx=10, pady=10)

variable_north_and_south = tk.StringVar(window)
variable_north_and_south.set("N")
dropdown_north_and_south = tk.OptionMenu(window, variable_north_and_south, "N", "S")
dropdown_north_and_south.grid(row=1, column=1, padx=10, pady=10)

entry_lat_degrees = tk.Entry(window, width=5)
entry_lat_degrees.grid(row=1, column=2, padx=10, pady=10)
label_Degrees = tk.Label(window, text="° ")
label_Degrees.grid(row=1, column=3, padx=10, pady=10)

entry_lat_minutes = tk.Entry(window, width=5)
entry_lat_minutes.grid(row=1, column=4, padx=10, pady=10)
label_Minutes = tk.Label(window, text="’")
label_Minutes.grid(row=1, column=5, padx=10, pady=10)

entry_lat_seconds = tk.Entry(window, width=7)
entry_lat_seconds.grid(row=1, column=6, padx=10, pady=10)
label_Seconds = tk.Label(window, text="’’")
label_Seconds.grid(row=1, column=7, padx=10, pady=10)

# 创建标签和转换结果（输出部分）
label_decimal_latitude = tk.Label(window, text="Decimal：")
label_decimal_latitude.grid(row=2, column=0, padx=10, pady=10)
decimal_latitude_text_1 = tk.StringVar()
label_decimal_latitude_result = tk.Entry(window, textvariable=decimal_latitude_text_1, state='readonly')
label_decimal_latitude_result.grid(row=2, column=1, columnspan=7, padx=10, pady=10)
label_decimal_latitude_result.bind("<Button-3>", lambda e: copy_to_clipboard(decimal_latitude_text_1.get()))

# 创建标签、输入框和按钮（经度部分）
label_longitude = tk.Label(window, text="Longitude：")
label_longitude.grid(row=3, column=0, padx=10, pady=10)

variable_east_or_west = tk.StringVar(window)
variable_east_or_west.set("E")
dropdown_east_or_west = tk.OptionMenu(window, variable_east_or_west, "E", "W")
dropdown_east_or_west.grid(row=3, column=1, padx=10, pady=10)

entry_lon_degrees = tk.Entry(window, width=5)
entry_lon_degrees.grid(row=3, column=2, padx=10, pady=10)
label_Degrees = tk.Label(window, text="° ")
label_Degrees.grid(row=3, column=3, padx=10, pady=10)

entry_lon_minutes = tk.Entry(window, width=5)
entry_lon_minutes.grid(row=3, column=4, padx=10, pady=10)
label_Minutes = tk.Label(window, text="’")
label_Minutes.grid(row=3, column=5, padx=10, pady=10)

entry_lon_seconds = tk.Entry(window, width=7)
entry_lon_seconds.grid(row=3, column=6, padx=10, pady=10)
label_Seconds = tk.Label(window, text="’’")
label_Seconds.grid(row=3, column=7, padx=10, pady=10)

# 创建标签和转换结果（输出部分）
label_decimal_longitude = tk.Label(window, text="Decimal：")
label_decimal_longitude.grid(row=4, column=0, padx=10, pady=10)
decimal_longitude_text_1 = tk.StringVar()
label_decimal_longitude_result = tk.Entry(window, textvariable=decimal_longitude_text_1, state='readonly')
label_decimal_longitude_result.grid(row=4, column=1, columnspan=7, padx=10, pady=10)
label_decimal_longitude_result.bind("<Button-3>", lambda e: copy_to_clipboard(decimal_longitude_text_1.get()))

# 创建按钮并绑定事件
convert_button = tk.Button(window, text="Conversion", command=convert_coordinates_1)
convert_button.grid(row=5, column=0, columnspan=8, padx=10, pady=10)

# Create label (Decimal to Degrees, Minutes, Seconds)
label_title = tk.Label(window, text="Decimal Coordinate Conversion to Degree-Minute-Second Coordinate (for Runways)：")
label_title.grid(row=6, column=0, columnspan=8, padx=10, pady=10)

# Create label and input box (Latitude part)
label_latitude = tk.Label(window, text="Decimal latitude：")
label_latitude.grid(row=7, column=0, padx=10, pady=10)
entry_lat_latitude = tk.Entry(window)
entry_lat_latitude.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

# Create label and result display (Output part)
label_decimal_latitude = tk.Label(window, text="Latitude：")
label_decimal_latitude.grid(row=8, column=0, padx=10, pady=10)
decimal_latitude_text = tk.StringVar()
label_decimal_latitude_result = tk.Entry(window, textvariable=decimal_latitude_text, state='readonly')
label_decimal_latitude_result.grid(row=8, column=1, columnspan=3, padx=10, pady=10)
label_decimal_latitude_result.bind("<Button-3>", lambda e: copy_to_clipboard(decimal_latitude_text.get()))

# Create label and input box (Longitude part)
label_longitude = tk.Label(window, text="Decimal Longitude：")
label_longitude.grid(row=9, column=0, padx=10, pady=10)
entry_lat_longitude = tk.Entry(window)
entry_lat_longitude.grid(row=9, column=1, columnspan=3, padx=10, pady=10)

# Create label and result display (Output part)
label_decimal_longitude = tk.Label(window, text="Longitude：")
label_decimal_longitude.grid(row=10, column=0, padx=10, pady=10)
decimal_longitude_text = tk.StringVar()
label_decimal_longitude_result = tk.Entry(window, textvariable=decimal_longitude_text, state='readonly')
label_decimal_longitude_result.grid(row=10, column=1, columnspan=3, padx=10, pady=10)
label_decimal_longitude_result.bind("<Button-3>", lambda e: copy_to_clipboard(decimal_longitude_text.get()))

# Create button and bind event
convert_button = tk.Button(window, text="Conversion", command=convert_coordinates_2)
convert_button.grid(row=11, column=0, columnspan=8, padx=10, pady=10)

# 运行GUI主循环
window.mainloop()
