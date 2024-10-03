<template lang="html">
    <div class="header">
        <img class="logo" src="./assets/logo1.png" alt="logo">
    </div>
</template>

<script>

export default {

}
</script>

<style lang="css" scoped>
    .logo{
        width: 250px;
        transition: transform 0.3s;
    }
    .logo:hover{
        transform: scale(1.05);
        transition: transform 0.3s;
    }
</style>