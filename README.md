# Galton_Plate

2021-03-26  新作 | New Project

using python file to simulate Galton Plate

  上个星期才搞了一份代码，本来以为灵感就此枯竭，没想到周二的热学课就看到了书上的伽尔顿板（Galton Plate），于是兴致盎然的开始肝(拒绝内卷，从我做起[手动滑稽])，应该还未完成，还想加点绘制柱形图或折线图的功能。

  I just finished my first project (in GitHub) last week, so it surprised me when I thought"How about simulate Galton Plate?" when taking a thermology course. Incomplete,want to add some functions like showing column diagram based on data.

------------------------------------------------------------------------------------------------------------------------

2021-03-28  更新 | Update

优化代码，调整个别语句块，为减少计算负担，每个落点只显示一个小球。
新增手动输入添加小球的功能：输入你想添加的小球数目，点击“Run”按钮即可。

Code improved. In order to lessen computor's burden, I only show one ball in one place.
An "Run" bottom is available now, input number in the "Add" box and press "Run" to see what will happen!

------------------------------------------------------------------------------------------------------------------------

2021-05-31  更新 | Update

修复使用Finish快速结束添球时的BUG（问题在int函数是取整数部分而非向下取整）。
新增绘图功能：点击“Draw”，通过matplotlib库绘制折线图。

Repair the BUG on "Finish" buttom (with some little place-changes when using "int").
Add buttom "Draw", with which we can form a chart easily.
