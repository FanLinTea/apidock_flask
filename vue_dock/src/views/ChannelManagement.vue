<template>
    <div class="top">
      <!--导航栏-->
      <div style="height: 70px;margin-left: 20px;background-color: #ffffff;box-shadow:1px 1px 5px 1px #e0e0e0;">
        <mu-auto-complete v-model="top_mu_company"  open-on-focus
                       placeholder="渠道名 or 渠道id......"
                       class="mu_input" style="width: 220px"
                       :max-search-results="5"
                       :data="input_data.channels"
                       ></mu-auto-complete>
        <mu-auto-complete :data="input_data.citys" placeholder="城市"
                          :max-search-results="5"  v-model="top_mu_city"
                          open-on-focus class="mu_input"
                          style="width: 140px"></mu-auto-complete>
        <mu-button round color="#1503EF" style="margin-top: 20px;margin-left:24px;max-height: 32px" class="mu_input" @click="search">搜索</mu-button>
        <!--头像-->
        <mu-menu cover placement="bottom-end" style="margin-top: 8px;float: right;margin-right: 30px">
          <span style="float: left;margin-right: 20px;margin-top: 20px;font-size: 16px;color: #757575">诸葛找房</span>
          <mu-button icon fab style="max-width: 50px;max-height: 50px">
             <img src="../assets/timg.jpg" style="max-width: 52px;">
          </mu-button>
          <mu-list slot="content">
            <mu-list-item button>
              <mu-list-item-title>个人信息</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
              <mu-list-item-title>退出登陆</mu-list-item-title>
            </mu-list-item>
          </mu-list>
        </mu-menu>
        <!---->
      </div>
      <!---->
      <div style="padding: 20px;width: 100%;height: calc(100% - 70px);padding-bottom: 10px">
        <el-row style="height: 100%;width: 100%">
          <!--内容区域-->
          <el-col :span="7" style="overflow-y:auto;height:100%;">

            <mu-paper class="mu-paper" :z-depth="3" v-for="i in channels_left_label"
                      v-if="input_select_city && !input_select_channel" :key="i.id"
                      @mouseover="mouseover(i.id)" @mouseout="mouseout" @click="OpenDetails(i.id, i)"
                      :class="{'lab_sty2':label_style===i.id, 'lab_sty':label_style_click===i.id}">
              <p style="float: left;font-size: 18px;margin-left: 20px;margin-top: 28px;font-weight:bold;color: #424242;overflow: hidden;
text-overflow: ellipsis;white-space: nowrap;max-width: 40%;height: 20px;line-height:20px">{{i.source_name}}</p>
              <div style="float: right;height: 100%;margin-right: 30px;max-width: 40%;">
                <div style="display: inline-block;float: right;margin-left: 20px">
                  <p style="margin-top: 14px;float: right;color: #bdbdbd;">创建时间</p>
                  <p style="float: bottom;margin-top: 42px;font-size: 16px;color: #424242">{{i.ctime}}</p>
                </div>
              </div>
            </mu-paper>

            <mu-paper class="mu-paper" :z-depth="3" v-for="s in channels_left_label"  :key="s.city_name"
                      v-if="!input_select_city && input_select_channel || input_select_city && input_select_channel"
                      @mouseover="mouseover(s.city_name)" @mouseout="mouseout" @click="OpenDetails(s.city_name, s)"
                      :class="{'lab_sty2':label_style===s.city_name, 'lab_sty':label_style_click===s.city_name}">
              <p style="float: left;font-size: 18px;margin-left: 20px;margin-top: 28px;font-weight:bold;color: #424242">{{s.city_name}}</p>
              <div style="float: right;height: 100%;margin-right: 6%;max-width: 60%;">
                <div style="display: inline-block;float: right;margin-left: 26px">
                  <p style="margin-top: 14px;float: right;color: #bdbdbd;">入库数量</p>
                  <p style="float: bottom;margin-top: 42px;font-size: 16px;color: #424242">{{s.num}}</p>
                </div>
                <div style="display: inline-block;float: right;margin-left: 20px">
                  <p style="margin-top: 14px;float: right;color: #bdbdbd;">更新时间</p>
                  <p style="float: bottom;margin-top: 42px;font-size: 16px;color: #424242">{{s.time}}</p>
                </div>
              </div>
            </mu-paper>

          </el-col>
          <el-col :span="9" style="height:100%;margin-left: 30px">
            <mu-paper :z-depth="3" style="height: calc(100% - 14px);width: 98%;overflow-y:auto;" v-if="paper_details">
              <div style="width: 100%;margin-top: 20px;margin-left: auto;" class="block">
                  <el-date-picker
                    v-model="date_time"
                    type="daterange"
                    align="center"
                    value-format="yyyy-MM-dd"
                    unlink-panels
                    range-separator="至"
                    :start-placeholder="start_time"
                    :end-placeholder="ent_time"
                    @change="select_date"
                    :picker-options="pickerOptions2">
                  </el-date-picker>
                  <!--<p style="margin-top: 20px;float: left;color: #bdbdbd;">source_name</p>-->
                  <!--<div style="width: 100%;height: 6px;float: right"></div>-->
                  <!--<p style="float: left;margin:0;font-size: 16px;color: #424242;">quanzhou-ChuanglianfangchanRent</p>-->
              </div>
              <!--分割线-->
              <div style="width: 80%;height: 1px;background-color: #cfd8dc;display: inline-block"></div>
              <!--<p style="margin-bottom: 0">最近一次数据</p>-->
              <mu-paper :z-depth="3" style="height: 80px;width: 94%;margin:0 auto;margin-top: 10px;background: linear-gradient(to top right, #f50057, #283593, #1503EF);" class="color_paper">
                <div style="float: left;margin-left: 20px;">
                  <p style="margin-top: 20px;float: left;color: #cfd8dc;">gov量</p><br>
                  <p style="float: left;margin:0;font-size: 16px;color: #ffffff">{{ gov_num }}</p>
                </div>
                <div style="width: 1px;height: 20px;background-color: #ffffff;float: left;margin-left: 20px;margin-top: 16px"></div>
                <div style="float: left;margin-left: 20px;">
                  <p style="margin-top: 20px;float: left;color: #cfd8dc;">bad量</p><br>
                  <p style="float: left;margin:0;font-size: 16px;color: #ffffff">{{ bad_num }}</p>
                </div>

                <div style="float: right;width: 200px;height: 100%;margin-right: 30px;display: inline">
                  <p style="float: left;margin-left: 56px;margin-top: 34px;color: #ffffff;position:relative;">bad占比率</p>
                  <p style="color: #ffffff;position:relative;right: 6px;top:20px;float: right">{{bad_Proportion}}%</p>
                  <mu-circular-progress class="demo-circular-progress" mode="determinate" :value="progress" color="#ffffff" :stroke-width="8" :size="64" style="margin-top: 8px;position:relative;top:-42px;right: -10px;float: right"></mu-circular-progress>
                </div>
              </mu-paper>
              <div style="margin-top: 20px;width: 100%;height: 20px">
                <p style="float: left;color: #bdbdbd;margin-left: 20px;">bad详情</p>
              </div>
              <el-collapse style="width: 94%;margin: 30px auto 0 auto">
                <el-collapse-item v-for="i in bad_info">
                  <template slot="title" >
                    <div style="width: 100%">
                      <div style="float: left;">
                        <p style="font-size: 16px;color: #1503EF;float: left">{{ i.bad_type }}</p>
                        <p style="float: left;margin-top: 16px;margin-left: 5px">- bad类型</p>
                      </div>
                      <div style="float: right;margin-right: 20px">
                        <p style="font-size: 16px;color: #1503EF;float: left">{{ i.num }}</p>
                        <p style="float: left;margin-top: 16px;margin-left: 6px">- bad总量</p>
                      </div>
                    </div>
                  </template>
                  <div style="float: left;color: #ff5722;margin-top: -10px;width: 100%;">
                    <p style="color: #ff3d00;">
                      <mu-button color="error" style="float: left;margin-bottom: 10px" small>原数据示例</mu-button>
                      <span style="margin-left: 10px;">{{i.bad_info}}</span>
                    </p>
                  </div>
                </el-collapse-item>
              </el-collapse>
            </mu-paper>
            <p v-else style="margin-top: 40px;color: #757575">请点击左侧标签</p>
          </el-col>

          <el-col :span="7" style="height:100%;margin: 0;padding: 0;border: 0">
            <mu-flex justify-content="center" align-items="center" style="margin-left: 20px;margin-right: -20px;margin-top: 12px">
              <mu-button full-width color="blueGrey700"  v-if="!but" @click="but=true">查 询 全 城 市 bad</mu-button>
              <mu-button full-width color="#1503EF" v-else @click="but=false">下 载 bad 报 表</mu-button>
            </mu-flex>
            <mu-paper :z-depth="0" style="height: 30%;width: 100%;background-color: #ffffff;margin-left: 20px">
              <p>{{user_name}}</p>
              <p>{{source_name}}</p>
            </mu-paper>
            <mu-paper :z-depth="0" style="height: 30%;width: 100%;background-color: #ffffff;margin-left: 20px">
              <div style="width: 200px;height: 100%;"></div>

            </mu-paper>

          </el-col>

        </el-row>
      </div>
    </div>
</template>

<script>
    export default {
      name: "ChannelManagement",
      data() {
        return {
          but: false,
          progress: 0,
          activeIndex: '1',
          activeIndex2: '1',
          top_mu_company: '',
          top_mu_city: '',
          input_select_channel: '',
          input_select_city: '',
          top_mu_citys: ['北京','上海','乌鲁木齐'],
          paper_details: false,
          all_channel: [],
          input_data: {
            channels: [],
            citys: [],
            company_id: []
          },
          select_channels: [],
          select_citys: [],
          channels_left_label:[],
          label_style: false,
          label_style_click: false,
          gov_num: 0,
          bad_info: [],
          bad_num: 0,
          bad_Proportion: 0,
          pickerOptions2: {
            shortcuts: [{
              text: '最近一周',
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                picker.$emit('pick', [start, end]);
              }
            }, {
              text: '最近一个月',
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                picker.$emit('pick', [start, end]);
              }
            }, {
              text: '最近三个月',
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                picker.$emit('pick', [start, end]);
              }
            }]
          },
          date_time: '',
          start_time: null,
          ent_time: null,
          label_data: [],
          user_name: '',
          source_name: '',
        };
      },

      created() {
        this.all_channels()
      },

      methods: {

        //  所有渠道
        all_channels() {
          this.$apidoc.get('internalpage/all_channel').then( Response=> {
            this.all_channel = Response.data
            this.input_data.channels = this.all_channel.source_name
            this.input_data.citys = this.all_channel.city
          })
        },
        //  搜索渠道
        search() {
          let channel = this.top_mu_company
          let city = this.top_mu_city
          this.input_select_channel = channel
          this.input_select_city = city
          if (channel || city) {
              this.$apidoc.post('internalpage/select_channel', {'channel': channel, 'city': city}).then( Response => {
                if(Response.data.flag === 2) {
                  this.$toast.error(Response.data.message);
                }else {
                  this.channels_left_label = Response.data
                  console.log('===============',this.channels_left_label)
                }
              }).catch( error => {
                console.log(error)
              })
          }else {
            this.$toast.error('请填写渠道名 or 城市');
          }
        },
        // 左侧标签鼠标移入样式
        mouseover(data) {
            this.label_style = data
        },
        // 左侧标签鼠标移出样式
        mouseout() {
          this.label_style = false
        },
        //  bad 详情弹出框  and  bad比例
        OpenDetails(po, data) {
          this.paper_details = true
          this.label_style_click = po
          this.label_data = data
          this.user_name = data.user_name
          this.source_name = data.source_name
          console.log('label_style_click:',  this.label_style_click, data)
          this.progress = 0
          setTimeout(()=>this.progress=this.bad_Proportion ,500);
          data = {
                  'company_id': data.company_id,
                  'source':data.source,
                  'city_py':data.city_py
                 }
          this.$apidoc.post('internalpage/bad_info', data).then( Response => {
            console.log(Response.data)
            this.gov_num = Response.data.gov.count
            this.bad_info = Response.data.bad
            this.start_time = Response.data.gov.time
            this.ent_time = Response.data.gov.time
            let num = 0
            for (let i of this.bad_info) {
                num += i.num
            }
            this.bad_num = num
            this.bad_Proportion = parseInt(this.bad_num/(this.bad_num+this.gov_num)*100)
          })
        },
        //  时间选择器
        select_date() {
          console.log(this.date_time)
          let time = {'time': this.date_time, 'data': this.label_data}
          console.log(time)
          this.$apidoc.post('internalpage/select_time', time).then( Response => {
            this.gov_num = Response.data.gov.count
            let num = 0
            for (let i of Response.data.bad) {
                num += i.num
            }
            this.bad_num = num
            this.bad_info = Response.data.bad
            this.bad_Proportion = parseInt(this.bad_num/(this.bad_num+this.gov_num)*100)
          })
        },
        test() {
          console.log(this.top_mu_company)
        },
      }
    }
</script>

<style scoped>
  .top {
    width: 100%;
    height: 100%;
  }
  .el-menu-item {
    height: 70px;
    line-height: 70px;
  }
  .el-menu-demo {
    box-shadow:1px 1px 5px 1px #cfd8dc;
  }
  .mu_input {
    float: left;
    margin-left: 40px;
    margin-top: 16px
  }
  .mu-paper {
    margin-top: 14px;
    border-radius: 8px;
    width: 96%;
    height: 70px;
  }

  ::-webkit-scrollbar {
    margin-left: -20px;
    width: 8px;
  }
  ::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background: rgba(0,0,0,0.1);
  }
  p{
    color: #757575;
  }
  div{
    color: #424242;
  }
  .lab_sty {
    border-top:5px solid #f44336;
  }
  .lab_sty2 {
    border-top:5px solid #ffeb3b;
  }
</style>
