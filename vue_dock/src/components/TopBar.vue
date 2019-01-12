<template>
    <div class="top">

      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
               style="height: 70px;"
               active-text-color="#1503EF"	>
        <el-menu-item index="1">处理中心</el-menu-item>
        <el-menu-item index="2" disabled>消息中心</el-menu-item>
        <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
        <!--<button>-->
          <!--<mu-avatar slot="avatar">-->
            <!--<img src="../assets/timg.jpg" style="max-width: 80px">-->
          <!--</mu-avatar>-->
        <!--</button>-->
        <mu-menu cover placement="bottom-end" style="margin-top: 8px;float: right;margin-right: 30px">
          <mu-button icon fab style="max-width: 50px;max-height: 50px">
            <img src="../assets/timg.jpg" style="max-width: 90px;">
          </mu-button>

          <mu-list slot="content">
            <mu-list-item button>
              <mu-list-item-title>Refresh</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
              <mu-list-item-title>Send feedback</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
              <mu-list-item-title>Settings</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
              <mu-list-item-title>Help</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
              <mu-list-item-title>Sign out</mu-list-item-title>
            </mu-list-item>
          </mu-list>
        </mu-menu>
      </el-menu>
    </div>
</template>

<script>
    export default {
      name: "TopBar",
      data() {
        return {
            activeIndex: '1',
            activeIndex2: '1',
          };
        },
      methods: {
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
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
</style>
