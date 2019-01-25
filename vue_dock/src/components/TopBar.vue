 <!--导航栏-->
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
               style="height: 70px;"
               active-text-color="#1503EF"	>
        <!--头像-->
        <mu-menu cover placement="bottom-end" style="margin-top: 8px;float: right;margin-right: 30px">
          <mu-button icon fab style="max-width: 50px;max-height: 50px">
            <img src="../assets/1.jpg" style="max-width: 90px;">
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
      </el-menu>
      <!---->
