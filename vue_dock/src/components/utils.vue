<template>
    
</template>

<script>
    export default {
        name: "utils",
      methods:{
          sleep(numberMillis) {
            var now = new Date();
            var exitTime = now.getTime() + numberMillis;
            while (true) {
                now = new Date();
                if (now.getTime() > exitTime)
                    return;
            }
        }
      }

    }
</script>

<style scoped>

</style>
