<template>
    <div>
        <Menu>
            <MenuButton>
                Menu
            </MenuButton>
            <MenuItems>
                <MenuItem>
                    Detalles de la cuenta
                </MenuItem> 
                    
                <MenuItem>
                    Citas 
                </MenuItem>

                <MenuItem>
                    Reportes Médicos
                </MenuItem>

                <MenuItem>
                    Prescripciones
                </MenuItem>

                <MenuItem>
                    No se que es ese logo
                </MenuItem>
            </MenuItems>
        </Menu>
    </div>
</template>

<script>
    import Menu from './Menu.vue'
    import MenuButton from './MenuButton.vue'
    import MenuItems from './MenuItems.vue'
    import MenuItem from './MenuItem.vue'

    export default {
        components: {
            Menu,
            MenuButton,
            MenuItems,
            MenuItem
        }
};
</script>

