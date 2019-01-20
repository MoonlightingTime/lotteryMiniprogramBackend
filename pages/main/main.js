// pages/main/main.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    sweepstakes: [
      {
        swpstkId: 0,
        swpstkName: "第一次抽奖",
        prizeName: "华为 p20",
        prizeValue: "￥5388",
        lotteryTime: "2019-12-12",
        imagePath: "./merchandise/0.png"
      },
      {
        swpstkId: 1,
        swpstkName: "第二次抽奖",
        prizeName: "小米小爱音响",
        prizeValue: "￥299",
        lotteryTime: "2019-11-11",
        imagePath: "./merchandise/1.jpg"
      },
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  sweepstakesTap: function(event) {
    console.log(event)
    var num=event.target.id.replace(new RegExp('^'+'sweepstakes_'), '');
    var changer = this.data["sweepstakes"]

    var regex = new RegExp(' 还没开始$')
    if (changer[num]["name"].match(regex)==null){
      changer[num]["name"] += " 还没开始"
    }else{
      changer[num]["name"] = changer[num]["name"].replace(regex, '')
    }
    this.setData({
      sweepstakes: changer
    })
    // var change_key = `sweepstakes[${num}].name`
    // var change_value = `${this.data.sweepstakes[num]["name"]} 还没开始`
    // console.log(change_key, change_value)
    // this.setData({
    //   change_key: change_value
    // })
  }
})