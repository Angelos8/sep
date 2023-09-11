<template>
	<table class="table">
		<thead>
			<tr>
				<th scope="col">Version</th>
				<th scope="col">File Name</th>
				<th scope="col" v-if="admin">Document ID</th>
				<th scope="col">Date Uploaded</th>
				<th scope="col">Date Approved</th>
				<th scope="col">Status</th>
			</tr>
		</thead>
		<tbody class="table-group-divider">
			<tr v-for="doc in documents">
				<td>{{ doc.version }}</td>
				<td>{{ doc.fileName }}</td>
				<td v-if="admin">{{ doc.docID }}</td>
				<td>{{ doc.uploadDate }}</td>
				<td>{{ doc.apprDate }}</td>
				<td>{{ doc.status }}</td>
			</tr>
		</tbody>
	</table>
</template>

<script>
export default {
	props: {
		label: {
			type: String,
			required: true,
		},
		admin: {
			type: Boolean,
			required: true,
			default: false,
		},
	},
	computed: {
		classes() {
			return {
				'tbl': true,
				'tbl-admin': this.admin,
				'tbl-user': !this.admin,
			};
		},
	},
}
</script>