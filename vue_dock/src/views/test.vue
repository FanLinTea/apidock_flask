<template>
    <div>


    <mu-button v-for="i in rote">
        {{i.name}}
    </mu-button>


    </div>
</template>

<script>
export default {
    data() {
        return {
          test:'weijiao',
          rote: this.$router.options.routes[0].children,
        }
    },
  created() {
    console.log(this.$router.options.routes[0].children)
  }
}
</script>

<style>

  .demo-paper{
    width: 200px;
    height: 300px;
    background: wheat;
  }
</style>

