<template>
    <div class="app_con">
        <el-container>
          <el-aside width="140px">
            <my-menu></my-menu>
          </el-aside>
          <el-container>
            <el-main>
              <router-view></router-view>
            </el-main>
          </el-container>
        </el-container>
    </div>
</template>

<script>
import myMenu from '@/components/LeftMenu'
    export default {
        name: "home",
        components: {
            myMenu,
        }
    }
</script>

<style scoped>
.app_con{
    height: 100%;
    display: flex;
}
.el-header, .el-footer {
    background-color: #F7F7FF;
    color: #333;
    text-align: center;
    line-height: 60px;
    padding-right: 0;
    padding-left: 10px;
    -moz-box-shadow:1px 1px 5px 1px #cfd8dc inset;
    -webkit-box-shadow:1px 1px 5px 1px #cfd8dc inset;
    box-shadow:1px 1px 5px 1px #cfd8dc inset;
  }

.el-aside {
  background-color: #F7F7FF;
  color: #333;
  text-align: center;
  /*line-height: 200px;*/
}

.el-main {
  background-color: #F7F7FF;
  color: #333;
  text-align: center;
  line-height: 100%;
  padding: 0;
  -moz-box-shadow:1px 1px 5px 1px #ffffff inset;
  -webkit-box-shadow:1px 1px 5px 1px #cfd8dc inset;
  box-shadow:2px 1px 6px 1px #cfd8dc inset;
}
</style>
