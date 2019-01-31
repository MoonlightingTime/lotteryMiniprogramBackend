// pages/main/main.js

var viewState = Object.freeze({
  "waitRequest": 0, "successRequest": 1, "failRequest": 2
});

Page({

  /**
   * 页面的初始数据
   */
  data: {
    sweepstakes: [],
    backend: "",
    viewState: viewState.waitRequest
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var app = getApp();
    this.data.backend = app.globalData.backend;
    this.getSwpstkInfo();
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

  // TODO: 从后端获得所有的抽奖信息
  getSwpstkInfo: function () {
    var self = this;
    wx.request({
      url: this.data.backend + '/sweepstake/query_swpstk/',
      success: self.infoSuccessCallback,
      fail: self.infoFailCallBack
    });
  },

  infoSuccessCallback: function (res) {
    console.log(res);
    var self = this;
    self.setData({
      viewState: viewState.successRequest,
      sweepstakes: []
    });
    res.data.data.forEach(function (item, index) {
      item.loadImage = true;
      var lotteryDataTime = new Date(item.lotteryTime);
      item.lotteryTime = `${lotteryDataTime.toDateString()}\n${lotteryDataTime.toTimeString()}`;

      console.log(item);
      self.data.sweepstakes.push(item);
      var cnmwx = `sweepstakes[${index}]`;
      self.setData({[cnmwx]: item});

      self.loadSwpStkImage(index);
    });
    // this.setData({sweepstakes: this.data.sweepstakes});
  },

  infoFailCallBack: function (res) {
    console.log(res);
    this.setData({
      viewState: viewState.failRequest,
      errMsg: res.errMsg
    })
  },
  
  loadSwpStkImage: function (num) {
    var self = this;
    wx.downloadFile({
      url: `${self.data.backend}/images/${this.data.sweepstakes[num].demoImage}`,
      success: res => {
        console.log(res);
        self.data.sweepstakes[num].loadImage = false;
        self.data.sweepstakes[num].demoImage = res.tempFilePath;
        var cnmwx = `sweepstakes[${num}]`;
        this.setData({[cnmwx]: self.data.sweepstakes[num]});
      }
    })
  },

  participateInSwpstk: function (swpstkId) {
    var app = getApp();
    var self = this;
    wx.request({
      url: this.data.backend + '/participate/participate_in',
      data: {
        openid: app.globalData.userInfo.openid,
        swpstkId: swpstkId
      },
      success: self.participateInCallBack
    })
  },

  participateInCallBack: function (res) {
    console.log(res);
  }
})