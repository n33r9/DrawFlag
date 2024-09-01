# import turtle

# # Tạo màn hình và thiết lập
# wn = turtle.Screen()
# wn.title("Cờ Tổ Quốc Việt Nam")
# wn.bgcolor("white")

# # Tạo đối tượng vẽ
# pen = turtle.Turtle()
# pen.speed(3)

# # Hàm vẽ hình chữ nhật
# def draw_rectangle(color, width, height):
#     pen.begin_fill()
#     pen.fillcolor(color)
#     for _ in range(2):
#         pen.forward(width)
#         pen.right(90)
#         pen.forward(height)
#         pen.right(90)
#     pen.end_fill()

# # Vẽ nền đỏ
# pen.penup()
# pen.goto(-150, 100)  # Di chuyển đến vị trí bắt đầu
# pen.pendown()
# draw_rectangle("red", 300, 200)

# # Hàm vẽ sao vàng 5 cánh
# def draw_star(x, y, length):
#     pen.penup()
#     pen.goto(x, y)
#     pen.setheading(-72)  # Điều chỉnh góc để cánh sao đầu tiên đúng vị trí
#     pen.pendown()
#     pen.color("yellow")
#     pen.begin_fill()
#     for _ in range(5):
#         pen.forward(length)
#         pen.right(144)
#     pen.end_fill()

# # Vẽ sao vàng 5 cánh lớn
# draw_star(0, 50, 100)  # Điều chỉnh vị trí và kích thước sao cho hợp lý

# # Hoàn tất
# pen.hideturtle()
# wn.mainloop()
# =============================================================================================================================


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Kích thước lá cờ
width = 3
height = 2

# Tạo một hình chữ nhật đại diện cho lá cờ
fig, ax = plt.subplots(figsize=(15, 7))  

# Lấy kích thước màn hình của người dùng và điều chỉnh kích thước cửa sổ đồ thị
fig_manager = plt.get_current_fig_manager()
# fig_manager.window.setGeometry(0, 0, 1920, 1080)

# Tọa độ trung tâm của ngôi sao
center_x = width / 2
center_y = height / 2

# Bán kính của vòng tròn ngoại tiếp ngôi sao
outer_radius = height / 3

# Bán kính của vòng tròn nội tiếp ngôi sao
inner_radius = outer_radius * np.sin(np.pi / 10) / np.cos(np.pi / 5)


def star_points(center_x, center_y, outer_radius, inner_radius):
    points = []
    angle = np.pi / 2  
    
    for i in range(5):
        x_out = center_x + outer_radius * np.cos(angle)
        y_out = center_y + outer_radius * np.sin(angle)
        points.append([x_out, y_out])
        
        angle += np.pi / 5
        
        x_in = center_x + inner_radius * np.cos(angle)
        y_in = center_y + inner_radius * np.sin(angle)
        points.append([x_in, y_in])
        
        angle += np.pi / 5
    
    return np.array(points)

# Tạo các điểm của ngôi sao
star = star_points(center_x, center_y, outer_radius, inner_radius)

# Vẽ ngôi sao vàng
star_patch = plt.Polygon(star, color='#FFFF00', edgecolor='orange', linewidth=2)
ax.add_patch(star_patch)

# Cài đặt hiển thị
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect(1)
ax.axis('off')

# Thêm tiêu đề và văn bản với kiểu chữ hoa văn hơn và màu đỏ đô
plt.title("Lá Cờ Tổ Quốc Việt Nam", fontsize=18, pad=20, fontweight='bold', family='serif')
plt.text(width / 2, -0.2, "Chúc mừng ngày Quốc Khánh 2/9", 
         fontsize=20, ha='center', va='center', color='#8B0000',  # Màu đỏ đô
         fontweight='bold', family='serif', style='italic')  # Kiểu chữ hoa văn hơn

# Hàm cập nhật để tạo hiệu ứng cờ bay phấp phới
def update(frame):
    # Hiệu ứng cờ bay phấp phới
    wave_offset_x = 0.03 * np.sin(frame / 10)
    wave_offset_y = 0.03 * np.cos(frame / 15)
    
    # Di chuyển cả ngôi sao và khung lá cờ
    ax.clear()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect(1)
    ax.axis('off')
    
    # Vẽ lại nền cờ với vị trí thay đổi
    ax.add_patch(plt.Rectangle((wave_offset_x, wave_offset_y), width, height, color='#DA251D'))

    # Vẽ lại ngôi sao với vị trí thay đổi
    transformed_star = star_points(center_x + wave_offset_x, center_y + wave_offset_y, outer_radius, inner_radius)
    star_patch.set_xy(transformed_star)
    ax.add_patch(star_patch)

    # Vẽ lại văn bản
    plt.text(width / 2, -0.2, "Chúc mừng ngày Quốc Khánh 2/9", 
             fontsize=20, ha='center', va='center', color='#8B0000',  # Màu đỏ đô
             fontweight='bold', family='serif', style='italic')  # Kiểu chữ hoa văn hơn

# Animation cho hiệu ứng phấp phới
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Đợi 2 giây trước khi bắt đầu animation
plt.pause(2)

# Hiển thị animation
plt.show()
