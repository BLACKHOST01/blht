# # import matplotlib.pyplot as plt
# # import io
# # import base64

# # def generate_sparkline(data):
# #     plt.figure(figsize=(2, 0.5))
# #     plt.plot(data)
# #     plt.axis('off')
    
# #     buffer = io.BytesIO()
# #     plt.savefig(buffer, format='png', transparent=True)
# #     buffer.seek(0)
# #     image_png = buffer.getvalue()
# #     buffer.close()
    
# #     graphic = base64.b64encode(image_png).decode('utf-8')
# #     return f'<img src="data:image/png;base64,{graphic}" />'
# import matplotlib.pyplot as plt
# import io
# import base64

# def generate_sparkline(data):
#     fig, ax = plt.subplots(figsize=(2, 0.5))
#     ax.plot(data)
#     ax.axis('off')
    
#     buffer = io.BytesIO()
#     fig.savefig(buffer, format='png', transparent=True)
#     plt.close(fig)  # Close the figure
    
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()
    
#     graphic = base64.b64encode(image_png).decode('utf-8')
#     return f'<img src="data:image/png;base64,{graphic}" />'
def generate_sparkline(data):
    if not data:
        return ''

    min_value = min(data)
    max_value = max(data)
    value_range = max_value - min_value if max_value > min_value else 1

    points = []
    for i, value in enumerate(data):
        x = i / (len(data) - 1) * 100
        y = 100 - ((value - min_value) / value_range * 100)
        points.append(f"{x},{y}")

    svg = f'''
    <svg width="100" height="30" viewBox="0 0 100 30" xmlns="http://www.w3.org/2000/svg">
        <polyline
            fill="none"
            stroke="#38b2ac"
            stroke-width="2"
            points="{' '.join(points)}"
        />
    </svg>
    '''
    return svg
