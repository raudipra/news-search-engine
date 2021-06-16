<template>
  <q-footer :class="['bg-primary', 'text-white']">
    <div class="row justify-center items-center q-mt-lg q-pt-lg">
      <div :class="['col-12', 'col-md-3', 'text-center q-mb-sm']">
        <span class="title text-h5 text-uppercase os-font">News Search Engine</span>
      </div>
    </div>
    <div class="row justify-center q-mt-sm q-mb-sm">
      <div :class="['col-12', 'col-md-3', 'text-center q-mb-sm']">
        <q-btn
          v-for="media in socialMedia"
          :key="media.icon"
          dense
          flat
          type="a"
          :href="media.link"
          target="_blank"
          class="q-mx-xs"
        >
          <q-avatar size="24px" square>
            <img :src="media.icon" />
          </q-avatar>
        </q-btn>
      </div>
    </div>
    <div :class="['row', 'justify-center', 'items-center', 'q-mb-lg', 'text-center']">
      <span>© 2021 by Praditya Raudi | All Rights Reserved</span>
    </div>
  </q-footer>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {
      socialMedia: [
        { icon: 'icons/github.svg', link: 'https://github.com/raudipra' },
        { icon: 'icons/linkedin.svg', link: 'https://www.linkedin.com/in/praditya-raudi-474a2912b/' },
        { icon: 'icons/gmail.svg', link: 'mailto: pra2118@columbia.edu' }
      ]
    }
  }
}
</script>

<style lang="sass" scoped>
.title
  letter-spacing: 0.1em
</style>
