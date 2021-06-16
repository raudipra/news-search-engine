<template>
  <q-page class="flex flex-center">
    <div class="container">
      <div class="row">
        <SearchBar
          ref="searchBar"
          @clicked="onClickSearch"
        />
      </div>

      <div class="row">
        <NewsList
          :items="newsItems"/>
      </div>

      <div class="row q-pa-lg flex flex-center">
        <q-pagination
          v-model="page"
          color="primary"
          :max="numPages"
          :max-pages="6"
          boundary-numbers
          @click="search()"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
import NewsList from 'components/wrapper/NewsList.vue'
import SearchBar from 'components/wrapper/SearchBar.vue'

export default {
  name: 'PageIndex',
  components: {
    NewsList,
    SearchBar
  },
  data () {
    return {
      page: 1,
      numPages: 0,
      newsItems: []
    }
  },
  methods: {
    search () {
      this.$refs.searchBar.search(this.page)
    },
    onClickSearch (page) {
      this.page = page
      this.numPages = this.$refs.searchBar.numPages
      this.newsItems = this.$refs.searchBar.newsItems
    }
  }
}
</script>
