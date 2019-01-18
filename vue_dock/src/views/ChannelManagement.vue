<template>
    <div class="top">
      <!--导航栏-->
      <div style="height: 70px;margin-left: 20px;background-color: #ffffff;box-shadow:1px 1px 5px 1px #e0e0e0;">
        <mu-text-field v-model="top_mu_company" placeholder="渠道名 or 渠道id......" class="mu_input" style="width: 220px"></mu-text-field>
        <mu-auto-complete :data="top_mu_citys" placeholder="城市" :max-search-results="5"  v-model="top_mu_city" open-on-focus class="mu_input" style="width: 140px"></mu-auto-complete>
        <mu-button round color="#1503EF" style="margin-top: 20px;margin-left:24px;max-height: 32px" class="mu_input" @click="test">搜索</mu-button>
        <!--头像-->
        <mu-menu cover placement="bottom-end" style="margin-top: 8px;float: right;margin-right: 30px">
          <span style="float: left;margin-right: 20px;margin-top: 20px;font-size: 16px;color: #757575">诸葛找房</span>
          <mu-button icon fab style="max-width: 50px;max-height: 50px">
             <img src="../assets/timg.jpg" style="max-width: 90px;">
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
            <mu-paper class="mu-paper" :z-depth="3" v-for="i in 15" @click="OpenDetails">
              <p style="float: left;font-size: 18px;margin-left: 20px;margin-top: 28px;font-weight:bold;color: #424242">北京</p>
              <div style="float: right;height: 100%;margin-right: 30px;width: 200px;">
                <div style="display: inline-block;float: right;margin-left: 26px">
                  <p style="margin-top: 12px;float: right;color: #bdbdbd;">房源类型</p>
                  <p style="float: bottom;margin-top: 44px;font-size: 16px;color: #424242">公寓</p>
                </div>
                <div style="display: inline-block;float: right;margin-left: 20px">
                  <p style="margin-top: 12px;float: right;color: #bdbdbd;">拥有者</p>
                  <p style="float: bottom;margin-top: 44px;font-size: 16px;color: #424242">汪洋</p>
                </div>
              </div>
            </mu-paper>
          </el-col>
          <el-col :span="9" style="height:100%;margin-left: 30px">

            <mu-paper :z-depth="3" style="height: calc(100% - 14px);width: 98%;overflow-y:auto;" v-if="paper_details">
              <div style="float: left;margin-left: 20px;width: 90%">
                  <p style="margin-top: 20px;float: left;color: #bdbdbd;">source_name</p>
                  <div style="width: 100%;height: 6px;float: right"></div>
                  <p style="float: left;margin:0;font-size: 16px;color: #424242;">quanzhou-ChuanglianfangchanRent</p>

              </div>
              <!--分割线-->
              <div style="width: 94%;height: 1px;background-color: #cfd8dc;display: inline-block"></div>

              <mu-paper :z-depth="3" style="height: 80px;width: 94%;margin:0 auto;margin-top: 10px;background: linear-gradient(to top right, #f50057, #283593, #1503EF);" class="color_paper">
                <div style="float: left;margin-left: 20px;">
                  <p style="margin-top: 20px;float: left;color: #cfd8dc;">gov量</p><br>
                  <p style="float: left;margin:0;font-size: 16px;color: #ffffff">22222</p>
                </div>
                <div style="width: 1px;height: 20px;background-color: #ffffff;float: left;margin-left: 20px;margin-top: 16px"></div>
                <div style="float: left;margin-left: 20px;">
                  <p style="margin-top: 20px;float: left;color: #cfd8dc;">bad量</p><br>
                  <p style="float: left;margin:0;font-size: 16px;color: #ffffff">3435</p>
                </div>

                <div style="float: right;width: 200px;height: 100%;margin-right: 30px;display: inline">
                  <p style="float: left;margin-left: 56px;margin-top: 34px;color: #ffffff;position:relative;">bad占比率</p>
                  <p style="color: #ffffff;position:relative;right: 6px;top:20px;float: right">80%</p>
                  <mu-circular-progress class="demo-circular-progress" mode="determinate" :value="progress" color="#ffffff" :stroke-width="8" :size="64" style="margin-top: 8px;position:relative;top:-42px;right: -10px;float: right"></mu-circular-progress>
                </div>
              </mu-paper>
              <div style="margin-top: 20px;width: 100%;height: 20px">
                <p style="float: left;color: #bdbdbd;margin-left: 20px;">bad详情</p>
              </div>
              <el-collapse v-model="activeNames" @change="handleChange" style="width: 94%;margin: 30px auto 0 auto">
                <el-collapse-item v-for="i in 10">
                  <template slot="title" >
                    <div style="width: 100%">
                      <div style="float: left;">
                        <p style="font-size: 16px;color: #1503EF;float: left">17</p>
                        <p style="float: left;margin-top: 16px;margin-left: 5px">- bad类型</p>
                      </div>
                      <div style="float: right;margin-right: 20px">
                        <p style="font-size: 16px;color: #1503EF;float: left">4321</p>
                        <p style="float: left;margin-top: 16px;margin-left: 6px">- bad总量</p>
                      </div>
                    </div>
                  </template>
                  <div style="float: left;font-family: 'PingFang SC';color: #ff5722;margin-top: -10px;width: 90%;margin-left: 20px">
                    <p style="float: left;color: #bdbdbd;margin-right: 10px;margin-left: 10px">bad解析:</p>
                    <p style="color: #ff3d00;float: left">小区名&室&总楼层&价格&城区&商圈 不能为空</p>
                  </div>
                </el-collapse-item>
              </el-collapse>
            </mu-paper>
            <p v-else style="margin-top: 40px;color: #757575">请点击城市标签</p>
          </el-col>

          <el-col :span="7" style="height:100%;margin: 0;padding: 0;border: 0">
            <mu-flex justify-content="center" align-items="center" style="margin-left: 20px;margin-right: -20px;margin-top: 12px">
              <mu-button full-width color="blueGrey700"  v-if="!but" @click="but=true">查 询 全 城 市 bad</mu-button>
              <mu-button full-width color="#1503EF" v-else @click="but=false">下 载 bad 报 表</mu-button>
            </mu-flex>
            <mu-paper :z-depth="0" style="height: 30%;width: 100%;background-color: #ffffff;margin-left: 20px">

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
          progress: '',
            activeIndex: '1',
            activeIndex2: '1',
            top_mu_company: '',
            top_mu_city: '',
            top_mu_citys: ['北京','上海','乌鲁木齐'],
            paper_details: false,
          };
        },
      methods: {
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
        },
        OpenDetails() {
          this.paper_details = true

          setTimeout(()=>this.progress=80 ,500);
        },
        test() {
          let a = {
            "name": "wang"
          }
          this.$apidoc.post('internalpage/select_channel', a).then(r => {
            console.log(r)
          }).catch(error => {
            console.log(error)
          })
        }
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
</style>
