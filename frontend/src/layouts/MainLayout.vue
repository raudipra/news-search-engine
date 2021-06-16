<template>
  <q-layout view="hHh lpR fff">
    <q-page-container>
      <router-view />
    </q-page-container>

    <Footer/>
  </q-layout>
</template>

<script>
import Footer from 'components/base/Footer.vue'

export default {
  components: {
    Footer
  }
}
</script>
