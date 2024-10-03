<template lang="html">
    <div>
        <slot :is-open = "isOpen"/>  
    </div>
</template>

<script>

    export default {
        data() {
            return {
                isOpen: true,
            }
        },

        methods: {
            open() {
                this.isOpen = true;
            },
            close() {
                this.isOpen = false;
            },
            toggle() {
                this.isOpen = !this.isOpen;
            }
        }
    }
</script>

<style lang="css" scoped>
    div {
        color: white;
    }
</style>