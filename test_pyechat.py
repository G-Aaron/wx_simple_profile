from pyecharts import Polar

angle = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add(
    "",
    [1, 2, 3, 4, 3, 5, 1],
    angle_data=angle,
    type="barAngle",
    is_stack=True,
)
polar.add(
    "",
    [2, 4, 6, 1, 2, 3, 1],
    angle_data=angle,
    type="barAngle",
    is_stack=True,
)
polar.add(
    "",
    [1, 2, 3, 4, 1, 2, 5],
    angle_data=angle,
    type="barAngle",
    is_stack=True,
)
polar.render('1.html')