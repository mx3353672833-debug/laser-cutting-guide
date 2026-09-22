# 01 先认清屏幕

[简体中文](./01-ui-tour.md) | [English](../../en/learn/01-ui-tour.md)

截图来自柏楚官方 CypCut 教程。你装的是 E 或 Pro，排布可能不一样，逻辑一样。按钮名以你屏幕上写的为准。

屏幕大概分五块：

```text
┌────────────────────────────────────┐
│ 菜单（文件 绘图 工艺 数控…）         │
├────────────────────────────────────┤
│           绘图板                    │
├────────────────────────────────────┤
│ 控制台（开始 暂停 停止…）            │
│ 报警栏                              │
└────────────────────────────────────┘
```

## 控制台

![控制台](../../../assets/screenshots/bochu-cypcut/control-panel.png)

开始：切了，出光。  
暂停：停住，可以沿路径进退。  
停止：这轮结束，头回预设位置。  
模拟：不动机床。  
走边框、空走：机床动，不出光。

## 坐标

![坐标](../../../assets/screenshots/bochu-cypcut/coordinates.png)

浮动坐标，零点在头现在站的位置。  
工件坐标，零点在床身某个固定点。  
上机先回原点，不然坐标系不靠谱。

## 加工前用的三个

![手动检查](../../../assets/screenshots/bochu-cypcut/manual-check.png)

手动开一下激光、气、指示光，点动看看轴。上电后先摸清楚机床听不听话。

![预览](../../../assets/screenshots/bochu-cypcut/preview-position.png)

预览：头、零件、行程范围摆在一起看一眼。

![边框空走](../../../assets/screenshots/bochu-cypcut/frame-border-dryrun.png)

Frame 走边框：外接方框，机床动。  
Border：最外轮廓，机床动。  
Dry Run 空走：完整刀路，机床动，不出光不出气。

## 工艺区

![工艺](../../../assets/screenshots/bochu-cypcut/technique-panel.png)

![图层](../../../assets/screenshots/bochu-cypcut/layer-cut.png)

每层可以单独设切割、穿孔参数。细节下一课。

## 报警

![报警](../../../assets/screenshots/bochu-cypcut/alarm-title.png)

报警红字：停。抄原文。查 [卡住手册](00-stuck.md)。查不动就停机找人，带上原文。

## 练三分钟

打开软件或演示模式。指出菜单、绘图板、控制台、报警栏。找模拟，别点开始。把开始/暂停/停止在你自己屏幕上的位置记下来。

过了就去 [02 导图](02-first-import.md)
