<template>
  <div id="app">
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <h2>Visualisation des données météo</h2>
        </div>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>