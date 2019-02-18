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
                  <p style="margin-top: 14px;float: right;color: #bdbdbd;">上线总量</p>
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
                  <p style="margin-top: 20px;float: left;color: #cfd8dc;">上线数量</p><br>
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
                      <mu-button color="error" style="float: left;margin-bottom: 10px" small @click="open_bad_info(i.bad_type)">原数据示例</mu-button>
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
            <mu-paper :z-depth="0" style="height:180px;width: 100%;background-color: #ffffff;margin-left: 20px">
              <p style="margin: 0;padding-top: 20px;font-weight: bold;font-size: 15px">拥有者</p>
              <div style="width: 20%;height: 1px;background-color: #cfd8dc;display: inline-block"></div>
              <p style="margin: 0;margin-top: 5px;font-size: 15px">{{user_name}}</p>
              <p style="margin: 0;margin-top:10px;padding-top: 20px;font-weight: bold;font-size: 15px">sourcename</p>
              <div style="width: 30%;height: 1px;background-color: #cfd8dc;display: inline-block"></div>
              <p style="margin: 0;margin-top: 5px;font-size: 15px">{{source_name}}</p>
            </mu-paper>
            <mu-paper :z-depth="0" style="height: 30%;width: 100%;background-color: #ffffff;margin-left: 20px">
              <div style="width: 200px;height: 100%;"></div>

            </mu-paper>
          </el-col>
        </el-row>

         <el-dialog
            :visible.sync="openSimple"
            fullscreen
            center>
              <mu-data-table height="560" :columns="columns"  :data="tableData" fit>
                <template slot-scope="scope">
                  <td>{{scope.row.id}}</td>
                  <td class="is-center">{{scope.row.bad_type}}</td>
                  <td class="is-center">{{scope.row.source}}</td>
                  <td class="is-center">{{scope.row.company_id}}</td>
                  <td class="is-center">{{scope.row.source_name}}</td>
                  <td class="is-center">{{scope.row.created}}</td>
                  <td class="is-center">{{scope.row.updated}}</td>
                  <td class="is-center">{{scope.row.company_name}}</td>
                  <td class="is-center">{{scope.row.house_title}}</td>
                  <td class="is-center">{{scope.row.borough_name}}</td>
                  <td class="is-center">{{scope.row.borough_id}}</td>
                  <td class="is-center">{{scope.row.borough_address}}</td>
                  <td class="is-center">{{scope.row.cityarea_id}}</td>
                  <td class="is-center">{{scope.row.cityarea2_id}}</td>
                  <td class="is-center">{{scope.row.rent_type}}</td>
                  <td class="is-center">{{scope.row.source_url}}</td>
                  <td class="is-center">{{scope.row.house_desc}}</td>
                  <td class="is-center">{{scope.row.tag_desc}}</td>
                  <td class="is-center">{{scope.row.house_totalarea}}</td>
                  <td class="is-center">{{scope.row.house_price}}</td>
                  <td class="is-center">{{scope.row.house_toward}}</td>
                  <td class="is-center">{{scope.row.house_room}}</td>
                  <td class="is-center">{{scope.row.owner_name}}</td>
                  <td class="is-center">{{scope.row.owner_phone}}</td>
                  <td class="is-center">{{scope.row.source_owner}}</td>
                  <td class="is-center">{{scope.row.service_phone}}</td>
                  <td class="is-center">{{scope.row.house_pic_unit}}</td>
                  <td class="is-center">{{scope.row.house_pic_layout}}</td>
                  <td class="is-center">{{scope.row.house_hall}}</td>
                  <td class="is-center">{{scope.row.house_toilet}}</td>
                  <td class="is-center">{{scope.row.house_kitchen}}</td>
                  <td class="is-center">{{scope.row.house_fitment}}</td>
                  <td class="is-center">{{scope.row.house_relet}}</td>
                  <td class="is-center">{{scope.row.house_floor}}</td>
                  <td class="is-center">{{scope.row.house_topfloor}}</td>
                  <td class="is-center">{{scope.row.app_url}}</td>
                  <td class="is-center">{{scope.row.wap_url}}</td>
                  <td class="is-center">{{scope.row.sex}}</td>
                  <td class="is-center">{{scope.row.into_house}}</td>
                  <td class="is-center">{{scope.row.pay_type}}</td>
                  <td class="is-center">{{scope.row.pay_method}}</td>
                  <td class="is-center">{{scope.row.tag}}</td>
                  <td class="is-center">{{scope.row.comment}}</td>
                  <td class="is-center">{{scope.row.house_number}}</td>
                  <td class="is-center">{{scope.row.deposit}}</td>
                  <td class="is-center">{{scope.row.house_configroom}}</td>
                  <td class="is-center">{{scope.row.house_configpub}}</td>
                  <td class="is-center">{{scope.row.is_ture}}</td>
                  <td class="is-center">{{scope.row.is_fill}}</td>
                  <td class="is-center">{{scope.row.is_contrast}}</td>
                  <td class="is-center">{{scope.row.chain_url}}</td>
                  <td class="is-center">{{scope.row.repeat_cnt}}</td>
                  <td class="is-center">{{scope.row.property_right_years}}</td>
                  <td class="is-center">{{scope.row.housing_years}}</td>
                  <td class="is-center">{{scope.row.visit_total_num}}</td>
                  <td class="is-center">{{scope.row.visit_num}}</td>
                  <td class="is-center">{{scope.row.public_time}}</td>
                  <td class="is-center">{{scope.row.visit_time}}</td>
                  <td class="is-center">{{scope.row.entry_time}}</td>
                  <td class="is-center">{{scope.row.lessor_name}}</td>
                  <td class="is-center">{{scope.row.apartment_type}}</td>
                  <td class="is-center">{{scope.row.apartment_house_type}}</td>
                  <td class="is-center">{{scope.row.room_number}}</td>
                  <td class="is-center">{{scope.row.floor_type}}</td>
                  <td class="is-center">{{scope.row.metro_info}}</td>
                  <td class="is-center">{{scope.row.house_price_scope}}</td>
                  <td class="is-center">{{scope.row.service_charge}}</td>
                  <td class="is-center">{{scope.row.housing_type}}</td>
                  <td class="is-center">{{scope.row.room_price}}</td>
                  <td class="is-center">{{scope.row.now_brand_apartment}}</td>
                  <td class="is-center">{{scope.row.room_sold_count}}</td>
                  <td class="is-center">{{scope.row.unit_count}}</td>

                </template>
              </mu-data-table>

          </el-dialog>
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
              text: '昨天',
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 1);
                end.setTime(end.getTime() - 3600 * 1000 * 24 * 1);
                picker.$emit('pick', [start, end]);
              }
            }, {
              text: '前天',
              onClick(picker) {
                const end = new Date();
                const start = new Date();
                start.setTime(start.getTime() - 3600 * 1000 * 24 * 2);
                end.setTime(end.getTime() - 3600 * 1000 * 24 * 2);
                picker.$emit('pick', [start, end]);
              }
            },{
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
          service_type: '',
          start_time: null,
          ent_time: null,
          label_data: [],
          user_name: '',
          source_name: '',
          openSimple: false,
          columns: [
              { title: 'id',name: 'id' },
              { title: 'bad_type', name: 'bad_type', align: 'center', sortable: true },
              { title: 'source', name: 'source', align: 'center', sortable: true },
              { title: 'company_id', name: 'company_id', align: 'center', sortable: true },
              { title: 'source_name', name: 'source_name', align: 'center', sortable: true },
              { title: 'created', name: 'created',  align: 'center', sortable: true },
              { title: 'updated', name: 'updated',  align: 'center', sortable: true },
              { title: 'company_name', name: 'company_name',  align: 'center', sortable: true },
              { title: 'house_title', name: 'house_title',  align: 'center', sortable: true },
              { title: 'borough_name', name: 'borough_name',  align: 'center', sortable: true },
              { title: 'borough_id', name: 'borough_id',  align: 'center', sortable: true },
              { title: 'borough_address', name: 'borough_address',  align: 'center', sortable: true },
              { title: 'cityarea_id', name: 'cityarea_id',  align: 'center', sortable: true },
              { title: 'cityarea2_id', name: 'cityarea2_id',  align: 'center', sortable: true },
              { title: 'rent_type', name: 'rent_type',  align: 'center', sortable: true },
              { title: 'source_url', name: 'source_url',  align: 'center', sortable: true },
              { title: 'house_desc', name: 'house_desc',  align: 'center', sortable: true },
              { title: 'tag_desc', name: 'tag_desc',  align: 'center', sortable: true },
              { title: 'house_totalarea', name: 'house_totalarea',  align: 'center', sortable: true },
              { title: 'house_price', name: 'house_price',  align: 'center', sortable: true },
              { title: 'house_toward', name: 'house_toward',  align: 'center', sortable: true },
              { title: 'house_room', name: 'house_room',  align: 'center', sortable: true },
              { title: 'owner_name', name: 'owner_name',  align: 'center', sortable: true },
              { title: 'owner_phone', name: 'owner_phone',  align: 'center', sortable: true },
              { title: 'source_owner', name: 'source_owner',  align: 'center', sortable: true },
              { title: 'service_phone', name: 'service_phone',  align: 'center', sortable: true },
              { title: 'house_pic_unit', name: 'house_pic_unit',  align: 'center', sortable: true },
              { title: 'house_pic_layout', name: 'house_pic_layout',  align: 'center', sortable: true },
              { title: 'house_hall', name: 'house_hall',  align: 'center', sortable: true },
              { title: 'house_toilet', name: 'house_toilet',  align: 'center', sortable: true },
              { title: 'house_kitchen', name: 'house_kitchen',  align: 'center', sortable: true },
              { title: 'house_fitment', name: 'house_fitment',  align: 'center', sortable: true },
              { title: 'house_relet', name: 'house_relet',  align: 'center', sortable: true },
              { title: 'house_floor', name: 'house_floor',  align: 'center', sortable: true },
              { title: 'house_topfloor', name: 'house_topfloor',  align: 'center', sortable: true },
              { title: 'app_url', name: 'app_url',  align: 'center', sortable: true },
              { title: 'wap_url', name: 'wap_url',  align: 'center', sortable: true },
              { title: 'sex', name: 'sex',  align: 'center', sortable: true },
              { title: 'into_house', name: 'into_house',  align: 'center', sortable: true },
              { title: 'pay_type', name: 'pay_type',  align: 'center', sortable: true },
              { title: 'pay_method', name: 'pay_method',  align: 'center', sortable: true },
              { title: 'tag', name: 'tag',  align: 'center', sortable: true },
              { title: 'comment', name: 'comment',  align: 'center', sortable: true },
              { title: 'house_number', name: 'house_number',  align: 'center', sortable: true },
              { title: 'deposit', name: 'deposit',  align: 'center', sortable: true },
              { title: 'house_configroom', name: 'house_configroom',  align: 'center', sortable: true },
              { title: 'house_configpub', name: 'house_configpub',  align: 'center', sortable: true },
              { title: 'is_ture', name: 'is_ture',  align: 'center', sortable: true },
              { title: 'is_fill', name: 'is_fill',  align: 'center', sortable: true },
              { title: 'is_contrast', name: 'is_contrast',  align: 'center', sortable: true },
              { title: 'chain_url', name: 'chain_url',  align: 'center', sortable: true },
              { title: 'repeat_cnt', name: 'repeat_cnt',  align: 'center', sortable: true },
              { title: 'property_right_years', name: 'property_right_years',  align: 'center', sortable: true },
              { title: 'housing_years', name: 'housing_years',  align: 'center', sortable: true },
              { title: 'visit_total_num', name: 'visit_total_num',  align: 'center', sortable: true },
              { title: 'visit_num', name: 'visit_num',  align: 'center', sortable: true },
              { title: 'public_time', name: 'public_time',  align: 'center', sortable: true },
              { title: 'visit_time', name: 'visit_time',  align: 'center', sortable: true },
              { title: 'entry_time', name: 'entry_time',  align: 'center', sortable: true },
              { title: 'lessor_name', name: 'lessor_name',  align: 'center', sortable: true },
              { title: 'apartment_type', name: 'apartment_type',  align: 'center', sortable: true },
              { title: 'apartment_house_type', name: 'apartment_house_type',  align: 'center', sortable: true },
              { title: 'room_number', name: 'room_number',  align: 'center', sortable: true },
              { title: 'floor_type', name: 'floor_type',  align: 'center', sortable: true },
              { title: 'metro_info', name: 'metro_info',  align: 'center', sortable: true },
              { title: 'house_price_scope', name: 'house_price_scope',  align: 'center', sortable: true },
              { title: 'service_charge', name: 'service_charge',  align: 'center', sortable: true },
              { title: 'housing_type', name: 'housing_type',  align: 'center', sortable: true },
              { title: 'room_price', name: 'room_price',  align: 'center', sortable: true },
              { title: 'now_brand_apartment', name: 'now_brand_apartment',  align: 'center', sortable: true },
              { title: 'room_sold_count', name: 'room_sold_count',  align: 'center', sortable: true },
              { title: 'unit_count', name: 'unit_count',  align: 'center', sortable: true },
          ],
          tableData: [

          ]
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
          this.service_type = data.service_type
          this.paper_details = true
          this.label_style_click = po
          this.label_data = data
          this.user_name = data.user_name
          this.source_name = data.source_name
          this.progress = 0
          setTimeout(()=>this.progress=this.bad_Proportion ,500);
          data = {
                  'company_id': data.company_id,
                  'source':data.source,
                  'city_py':data.city_py,
                  'service_type': this.service_type
                 }
          this.$apidoc.post('internalpage/bad_info', data).then( Response => {
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
          let time = {'time': this.date_time, 'data': this.label_data}
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
        open_bad_info(bad_type) {
          this.openSimple = true
          this.label_data.bad_type = bad_type
          if (this.date_time) {
            this.label_data.start_time = this.date_time[0]
            this.label_data.ent_time = this.date_time[1]
          }else {
            this.label_data.start_time = this.start_time
            this.label_data.ent_time = this.ent_time
          }
          this.$apidoc.post('internalpage/data_tab', this.label_data).then( Response => {
            this.tableData = Response.data
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
