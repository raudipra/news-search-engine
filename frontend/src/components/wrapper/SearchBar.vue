<template>
  <div class="flex flex-center q-mb-xl q-mt-xl">
    <q-input v-model="query" filled type="search" class="search-bar">
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>
    <q-btn :loading="loading" color="primary" @click="search(1)" class="search-button">
      Search
      <template v-slot:loading>
        <q-spinner-hourglass class="on-left" />
        Loading...
      </template>
    </q-btn>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data () {
    return {
      loading: false,
      query: '',
      numPages: 0,
      page: 1,
      pageSize: 10,
      sortBy: 'relevancy',
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
    async search (page) {
      try {
        this.loading = true
        this.page = page

        const response = await this.$http.get(`/search`, {
          params: this.newsParams
        })
        if (response.status) {
          this.newsItems = response.data.articles
          this.numPages = Math.ceil(response.data.totalResults / this.pageSize)
          this.loading = false
          this.$emit('clicked', this.page)
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
