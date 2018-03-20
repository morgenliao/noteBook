# 设置手柄和VR
### main Object List
<VR_Pawn>
<VR_GameMode>
<UI_Mat1>

********
## 初始设置
### 使用 Steam VR
1. 必须运行Room Setup
2. 单击 (播放) > (虚拟现实预览)
3. 确定 (Plugin) > (SteamVR)

********
### 蓝图
1. 创建 
    Pawn            -> VR_Pawn
    Game Mode Base  -> VR_GameMode
    
2. 修改
     <VR_GameMode>
    * Classes > Default Pawn Class => VR_Pawn
3. <世界设置> 面板
   GameMode > GameMode Override => VR_GameMode  


  
*********

### VR_Pawn
1. <VR_Pawn>
   <Detail>.面板
   <Camera> > <Base Eye Height> => 0.0
2. 组件标签中，添加<SteamVRChaperone>组件 //蓝色监护边框现实
3. <Camere>.组件
4. 将摄像机Transform Location 设定为（0，0,0）

### 玩家起始点
1. Z轴高度1.0cm //因为HMD的坐标识别原点是0,0,0，如果按照传统的设定为真人高度，会让VR摄像机出现偏差，使画面中的角色漂浮在地面之上。

### 移除Room的碰撞体
1. <碰撞> => <Remove Collision>

## 运动控制器设置
### 导入手柄模型
1. 在 <Room> -> 创建 <ControllerModel>.文件夹
2. 导入素材chapter14\shoubing.FBX
3. <VR_Pawn(BP)>, 添加组件，添加运动控制器组件（MotionController）
* ![](.img\001.png)

### 设置MotionController组件
1. 选中MotionController组件，命名为MotionController_left
2. <Detail>面板 > <Motion Controller>选项卡 <Hand> => left

### 添加Mesh
1. 在MotionController_Left子组件，添加Left Hand Mesh
2. Location（-7, 0, -10), Rotation(0,0,90), Scale (0.25, 0.25, 0.25)


**********
## 制作UI界面
### 创建UI_Mat1.控件蓝图
1. 创建<UI>.文件夹, 导入UI图片
* ![](.img\002.png)
2. Room> BP 创建<UI>.文件夹
3. 创建UI_Mat1.控件

### 修改UI_Mat1.控件蓝图
* ![](.img\003.png)
1. 修改尺寸为Custom，512X512
2. 铺满Canvas Panel
* ![](.img\004.png)


and <UI_Mat2>，<UI_Mat3>

### 设置VR_Pawn
在MotionController_Left.组件 添加 Widget.子组件
* ![](.img\005.png)

在 <项目设置>.选项卡 
输入 > Action Mappings
* ![](.img\006.png)
* ![](.img\007.png)

### 设置VR_Pawn蓝图
1. ![](.img\008.png)
> 让UI一开始处于隐藏状态

2. 让左手柄菜单键控制UI的打开和关闭
* ![](.img\010.png)

3. 在Right Hand Mesh上面，的 <Component Tag>.选项栏 
 ```添加 Hand``` 
* ![](.img\009.png)
 
4. 编辑 <OnComponentEndOverlap>.事件
* ![](.img\011.png)