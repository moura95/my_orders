<template>
  <div id="header">
    <ul>
      <li>
        <router-link to="/">Home</router-link>
      </li>
      <li>
        <router-link to="/company">Empresa</router-link>
      </li>
      <li>
        <router-link to="/product">Produtos</router-link>
      </li>
      <li>
        <router-link to="/order">Pedidos</router-link>
      </li>
    </ul>
  </div>
</template>

<style scoped>
#header {
  width: 100%;
  height: 130px;
  background: lightblue;
}

ul {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding-top: 2em;
}

li {
  color: black;
  list-style: none;
}
</style>
