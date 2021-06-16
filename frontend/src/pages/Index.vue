<template>
  <q-page class="flex flex-center">
    <div class="container">
      <div class="row flex flex-center q-mb-xl q-mt-xl">
        <q-input v-model="query" filled type="search" class="search-bar">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-btn :loading="loading" color="primary" @click="search(true)" class="search-button">
          Search
          <template v-slot:loading>
            <q-spinner-hourglass class="on-left" />
            Loading...
          </template>
        </q-btn>
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
          @click="search(false)"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
import NewsList from 'components/wrapper/NewsList.vue'

export default {
  name: 'PageIndex',
  components: {
    NewsList
  },
  data () {
    return {
      loading: false,
      query: '',
      numPages: 0,
      page: 1,
      pageSize: 10,
      sortBy: 'popularity',
      newsItems: []
    }
  },
  computed: {
    newsParams () {
        const params = new URLSearchParams()
        params.append('q', this.query)
        params.append('sortBy', this.sortBy)
        params.append('pageSize', this.pageSize)
        params.append('page', this.page)
        return params
    }
  },
  methods: {
    async search (isQuerySearch) {
      try {
        this.loading = true
        if (isQuerySearch) {
          this.page = 1
        }
        const response = await this.$http.get(`/search`, {
          params: this.newsParams
        })
        if (response.status) {
          console.log(response.data.totalResults)
          this.newsItems = response.data.articles
          this.numPages = Math.ceil(response.data.totalResults / this.pageSize)
          this.loading = false
        }
      } catch (error) {
        console.log(error)
        this.loading = false
      }
    },
  }
}
</script>
<style lang="sass" scoped>
.search-bar
  margin-right: 30px
  width: 600px

.search-button
  height: 50px
</style>
