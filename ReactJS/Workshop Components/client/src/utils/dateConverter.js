export default function DateConvertor(isoDate) {
    const option = { year: "numeric", month: "long", day: "numeric" }

    return new Date(isoDate).toLocaleDateString(undefined, option)
}